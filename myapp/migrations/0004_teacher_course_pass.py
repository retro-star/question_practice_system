# Generated by Django 4.0.1 on 2022-01-26 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_course_teacher_student_question_course_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='course_pass',
            field=models.IntegerField(choices=[(1, '待审核'), (2, '通过'), (3, '不通过')], default=1),
        ),
    ]
