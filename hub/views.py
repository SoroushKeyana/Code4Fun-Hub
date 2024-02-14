from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Project, ForumPost, ForumComment
from .forms import ProjectForm, ForumPostForm, ForumCommentForm, ForumCategoryForm, SearchForm
from django.http import HttpResponseForbidden
from .forms import SuperuserCreationForm
from django.contrib import messages
from django.db.models import Q



def home(request):
    context = {
        'is_homepage': True, 
    }
    return render(request, 'home.html', context)


@login_required
def project_list(request):
    projects = Project.objects.all().order_by('-created_at')  
    return render(request, 'project_list.html', {'projects': projects})


@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user  
            project.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'create_project.html', {'form': form})
    

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project_files = [project.project_file]
    print("Project Files:", project_files)

    is_owner = request.user == project.created_by

    return render(request, 'project_detail.html', {'project': project, 'project_files': project_files, 'is_owner': is_owner})


@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.user == project.created_by:
        if request.method == 'POST':
            form = ProjectForm(request.POST, instance=project)
            if form.is_valid():
                form.save()
                return redirect('project_detail', pk=project.pk)
        else:
            form = ProjectForm(instance=project)
        return render(request, 'edit_project.html', {'form': form, 'project': project})
    else:
        return HttpResponseForbidden("You don't have permission to edit this project.")

@login_required
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.user == project.created_by:
        if request.method == 'POST':
            project.delete()
            return redirect('project_list')
        return render(request, 'delete_project.html', {'project': project})
    else:
        return HttpResponseForbidden("You don't have permission to delete this project.")


@login_required
def forum_post_list(request):
    forum_posts = ForumPost.objects.all().order_by('-created_at')
    return render(request, 'forum_post_list.html', {'forum_posts': forum_posts})


@login_required
def forum_post_detail(request, post_id):
    post = get_object_or_404(ForumPost, pk=post_id)
    comments = ForumComment.objects.filter(post=post)

    is_owner = False  
    if request.user == post.created_by:
        is_owner = True

    if request.method == 'POST':
        comment_form = ForumCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('forum_post_detail', post_id=post.id)
    else:
        comment_form = ForumCommentForm()

    return render(request, 'forum_post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form, 'is_owner': is_owner})


@login_required
def create_forum_post(request):
    if request.method == 'POST':
        form = ForumPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.save()
            return redirect('forum_post_detail', post_id=post.id)
    else:
        form = ForumPostForm()
    return render(request, 'create_forum_post.html', {'form': form})


@login_required
def edit_forum_post(request, post_id):
    post = get_object_or_404(ForumPost, pk=post_id)

    if request.user == post.created_by:
        if request.method == 'POST':
            form = ForumPostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('forum_post_detail', post_id=post.id)
        else:
            form = ForumPostForm(instance=post)
        return render(request, 'edit_forum_post.html', {'form': form, 'post': post})
    else:
        return HttpResponseForbidden()

@login_required
def delete_forum_post(request, post_id):
    post = get_object_or_404(ForumPost, pk=post_id)

    if request.user == post.created_by:
        if request.method == 'POST':
            post.delete()
            return redirect('forum_post_list')
        return render(request, 'delete_forum_post.html', {'post': post})
    else:
        return HttpResponseForbidden()


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(ForumComment, pk=comment_id)
    if request.user == comment.user:
        if request.method == 'POST':
            form = ForumCommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('forum_post_detail', post_id=comment.post.id)
        else:
            form = ForumCommentForm(instance=comment)
        return render(request, 'edit_comment.html', {'form': form, 'comment': comment})
    else:
        return HttpResponseForbidden("You don't have permission to edit this comment.")

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(ForumComment, pk=comment_id)
    if request.user == comment.user:
        if request.method == 'POST':
            comment.delete()
            return redirect('forum_post_detail', post_id=comment.post.id)
        return render(request, 'delete_comment.html', {'comment': comment})
    else:
        return HttpResponseForbidden("You don't have permission to delete this comment.")



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful.')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field.capitalize()}: {error}')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to your desired page after successful login
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('home')


@login_required
def create_category(request):
    if request.user.is_staff:  
        if request.method == 'POST':
            form = ForumCategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('forum_post_list')
        else:
            form = ForumCategoryForm()
        return render(request, 'create_category.html', {'form': form})
    else:
        return redirect('forum_post_list')
    

@user_passes_test(lambda u: u.is_superuser)
def create_superuser(request):
    if request.method == 'POST':
        form = SuperuserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SuperuserCreationForm()

    return render(request, 'registration/create_super_user.html', {'form': form})

def search(request):
    query = request.GET.get('query', '')
    
    # Use Q objects to perform case-insensitive search across multiple fields
    projects = Project.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query) | Q(created_by__username__icontains=query)
    )

    forum_posts = ForumPost.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query) | Q(created_by__username__icontains=query)
    )

    print("Query:", query)
    print("Projects:", projects)
    print("Forum Posts:", forum_posts)

    context = {
        'query': query,
        'projects': projects,
        'forum_posts': forum_posts,
    }

    return render(request, 'search_results.html', context)