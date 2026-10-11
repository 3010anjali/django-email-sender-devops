
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import EmailForm


def send_email_view(request):
    sent = False

    if request.method == "POST":
        form = EmailForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=form.cleaned_data["subject"],
                message=form.cleaned_data["message"],
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[
                    form.cleaned_data["recipient_email"]
                ],
                fail_silently=False,
            )
            sent = True
            form = EmailForm()
    else:
        form = EmailForm()

    return render(
        request,
        "sender/email_form.html",
        {"form": form, "sent": sent},
    )
