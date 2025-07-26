from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def send_html_email(subject, template_name, context, to_email, from_email=None):
    """
    Send a beautiful HTML email using Django templates.
    
    Args:
        subject (str): Email subject
        template_name (str): Template name (e.g., 'users/emails/email_verification.html')
        context (dict): Context data for the template
        to_email (str): Recipient email address
        from_email (str): Sender email address (optional, uses DEFAULT_FROM_EMAIL if not provided)
    """
    if from_email is None:
        from_email = settings.DEFAULT_FROM_EMAIL
    
    # Render HTML content
    html_content = render_to_string(template_name, context)
    
    # Create plain text version by stripping HTML tags
    text_content = strip_tags(html_content)
    
    # Create email message
    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=from_email,
        to=[to_email]
    )
    
    # Attach HTML content
    email.attach_alternative(html_content, "text/html")
    
    # Send email
    email.send()


def send_verification_email(user, verification_link):
    """
    Send email verification email with beautiful template.
    
    Args:
        user: CustomUser instance
        verification_link (str): Email verification link
    """
    subject = "🎓 Welcome to E-Learning Platform - Verify Your Email"
    template_name = 'users/emails/email_verification.html'
    
    context = {
        'user_name': user.name,
        'verification_link': verification_link,
    }
    
    send_html_email(subject, template_name, context, user.email)


def send_password_reset_email(user, reset_link):
    """
    Send password reset email with beautiful template.
    
    Args:
        user: CustomUser instance
        reset_link (str): Password reset link
    """
    subject = "🔐 Reset Your Password - E-Learning Platform"
    template_name = 'users/emails/password_reset.html'
    
    context = {
        'user_name': user.name,
        'reset_link': reset_link,
    }
    
    send_html_email(subject, template_name, context, user.email)


def send_welcome_email(user):
    """
    Send welcome email with beautiful template after email verification.
    
    Args:
        user: CustomUser instance
    """
    subject = "🎉 Welcome to E-Learning Platform!"
    template_name = 'users/emails/welcome_email.html'
    
    context = {
        'user_name': user.name,
    }
    
    send_html_email(subject, template_name, context, user.email)


def send_password_reset_success_email(user):
    """
    Send password reset success email with beautiful template.
    
    Args:
        user: CustomUser instance
    """
    subject = "✅ Password Reset Successful - E-Learning Platform"
    template_name = 'users/emails/password_reset_success.html'
    
    context = {
        'user_name': user.name,
    }
    
    send_html_email(subject, template_name, context, user.email) 