#models.py
# .. import section ..
from datetime import timezone
from typing import List

from django.db import models


class Post(models.Model):
    author = models.ForeignKey(CustomUserModel)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=15000)
    is_published = models.BooleanField()


def try_to_send_emails_unpublished_posts(posts_ids: List[int], email_from='from@example.com') -> None:
    """
    Sends an email regarding post unpublished by author
    :param posts_ids: list of ids of posts that were unpublished
    :return: None
    """
    for post in Post.objects.filter(ids__in=posts_ids, is_published=False).prefetch_related['author']:
        send_email(
            'Notification',
            'Your article has been unpublished!',
            email_from,
            [post.author.email],
            fail_silently=False,
        )



######################################################
# To Do: How can we refactor code to make that faster?
######################################################

def func(user, moderator_ids):
    if user.pk in moderator_ids:
        Post.objects.all().update(updated_at=timezone.now())

#
######################################################


######################################################
# To Do: What problems can we encounter with? How can you impove the code?
######################################################

@transaction.atomic
def withdraw(user_id, amount):
    balance = UserBalance.objects.get(user_id=user_id)
    balance.amount -= amount
    balance.save()
    send_request_to_paypal(balance.paypal_id, amount)

#
######################################################


######################################################
# To Do:
# 1. Write a code of model `Webinar`, that contains the fields:
# - title
# - is_published
# - starts_at
#
# 2. Please, write a code of the function `get_nearest_webinar`. The function returns a published webinar that starts in the near future.
# 3. Write a code of the function `count_published_webinars`. That returns a number of published webinars.
# 4. How you could change the code if the count of published webinars is displayed on the really visited page?
#
# P.S.: If you need use additional classes you are welcome.
######################################################
class Webinar(models.Model):
    author = models.ForeignKey(CustomUserModel)
    is_published = models.BooleanField()
    starts_at = models.DateTimeField()

def get_nearest_webinar():
    return Webinar.objects.filter(starts_at__gte=timezone.now()).order_by('starts_at')[0]

def count_published_webinars():
    return Webinar.objects.filter(starts_at__lt=timezone.now()).count()

#
######################################################


######################################################
# Please, add the processing of probably exceptions and logging:
######################################################
#
@login_required()
def disable_subscription(request):
    try:
        account = Account.objects.get(user=request.user)
    except Account.DoesNotExists:
        logging.exception(f"Account for user {request.user} does not exists")

    if request.method == 'POST':
        if 'do_disable' in request.POST:
            account.switch_to_free()
            return HttpResponseRedirect(reverse('app:my_account'))

    return render(request, 'theme/disable_subscription.html')

#
######################################################


######################################################
# There is a really visited site. Many uWSGI workers. What problem will you probably encounter?
# What changes may you suggest?
######################################################
#


@transaction.atomic
def increment_views(webinar_id):
    # ...
    w = Webinar.objects.select_for_update().get(pk=webinar_id)
    w.views_count += 1
    w.save()
#...
#
######################################################
