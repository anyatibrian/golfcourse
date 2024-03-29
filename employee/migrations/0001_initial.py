# Generated by Django 2.1.4 on 2019-03-06 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaOfResidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(max_length=100)),
                ('town_council', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('length_of_current_residence', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='BankInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_bank', models.CharField(max_length=100, null=True)),
                ('bank_account_title', models.CharField(max_length=100, null=True)),
                ('account_number', models.CharField(max_length=100, null=True)),
                ('create_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CitizenshipInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('sub_county', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeePersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=100)),
                ('marital_status', models.CharField(choices=[('single', 'single'), ('married', 'married'), ('divorced', 'divorced'), ('cohabiting', 'cohabiting')], max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('number_of_children', models.IntegerField()),
                ('image', models.ImageField(default='avatar.jpg', null=True, upload_to='media/profile_pic')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_employed', models.DateTimeField()),
                ('current_job_title', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('employee_Id_number', models.CharField(max_length=100)),
                ('NSSF_number', models.CharField(max_length=30, null=True)),
                ('Tin_number', models.CharField(max_length=30, null=True)),
                ('created_at', models.DateTimeField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.EmployeePersonalInfo')),
            ],
        ),
        migrations.CreateModel(
            name='NextOfKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=100)),
                ('relationship', models.CharField(choices=[('sister', 'sister'), ('brother', 'brother'), ('wife', 'wife'), ('nephew', 'nephew'), ('niece', 'niece'), ('mother', 'mother'), ('father', 'father'), ('godFather', 'godFather'), ('cousin', 'cousin'), ('inlaw', 'inlaw')], max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.EmployeePersonalInfo')),
            ],
        ),
        migrations.AddField(
            model_name='citizenshipinfo',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.EmployeePersonalInfo'),
        ),
        migrations.AddField(
            model_name='bankinformation',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.EmployeePersonalInfo'),
        ),
        migrations.AddField(
            model_name='areaofresidence',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.EmployeePersonalInfo'),
        ),
    ]
