import smtplib

FROM = "John.Insider@gov.local"
TO = "Jane.Journalist@gov.local"

BODY = """\
From: John Insider <John.Insider@gov.local>
To: Jane.Journalist@gov.local
Subject: Urgent Update

-----BEGIN PGP MESSAGE-----

hF4D2zm/qzZ0vH0SAQdApPAUEjp5bl2B7uAZ/YxErl/S3HYWLlDeDuDjvgrQLgUw
saVOAzDQTtkN5hJetGA7lbtSfM5Em9JkCpWI7jgkQtB4SdEKM2bumT89WDjmhNRN
1MAfAQkCEBG71HcA74sWC99r1GekZN2cxxEEpGV0D0pbZKhFBCkHmKY5k6z+Ehj/
2JJ+QhNWaX+8yDOvjw8TT3DIwfNifV85JdCBOpJPfPZO7JmBn32OVWcJMennJ0We
Wcc0IQoSE6HzGvyXoT5Mwvh1x1s/q7emKcDtMOBjX5T9RqMdVK2a9PFpVYsj5UDx
3LUK/0GMoDavlbCJbnpUyfdGeB+ayV8IFf/fung58O6Fv9Idk/KDHlsxqqEGtFz7
OIfKjx6PFSC/0JNQNJfuMqrp1tj2Vm1Sn2NZZJ0RgEUPLA==
=1nOD
-----END PGP MESSAGE-----


"""

with smtplib.SMTP("gov.local", 25) as server:
    server.sendmail(FROM, [TO], BODY)
