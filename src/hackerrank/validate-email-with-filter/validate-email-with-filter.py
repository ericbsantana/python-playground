import re

mail_regex = re.compile(
    r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$')


def fun(s):
    return re.match(mail_regex, s)


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = 3
    emails = ['learn.point@learningpoint.net',
              'learnpoint@learningpoint.net',
              'learnpoint@learningpoint.net1']
    # for _ in range(n):
    #     emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
