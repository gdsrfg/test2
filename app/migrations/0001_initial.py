# Generated by Django 4.1.6 on 2023-03-12 02:08

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[('customer', 'customer'), ('tager', 'tager'), ('admin', 'admin')], max_length=50, verbose_name='نوع المستخدم ')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='اسم الاكسسوار')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image', verbose_name='Devices/Devices_Img/')),
                ('details', models.CharField(blank=True, max_length=200, null=True, verbose_name='التفاصيل')),
                ('color', models.CharField(blank=True, max_length=10, null=True, verbose_name='الون')),
                ('trade_mark', models.CharField(blank=True, max_length=10, null=True, verbose_name='العلامة التجارية')),
                ('price', models.IntegerField(verbose_name='السعر')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='Slug')),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='Slug')),
                ('name', models.CharField(choices=[('Samsung', 'Samsung'), ('Apple', 'Apple'), ('Huawei', 'Huawei'), ('Oppo', 'Oppo'), ('xiaomi', 'xiaomi'), ('Infinix', 'Infinix'), ('Nokia', 'Nokia'), ('Sony', 'Sony'), ('LG', 'LG'), ('HTC', 'HTC'), ('Lenovo', 'Lenovo'), ('Realme', 'Realme'), ('Honor', 'Honor'), ('ZTE', 'ZTE'), ('Vivo', 'Vivo'), ('Alcatel', 'Alcatel'), ('Asus', 'Asus'), ('Motorola', 'Motorola'), ('Acer', 'Acer'), ('Techno', 'Techno')], max_length=100, verbose_name='اسم البراند')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='brandslogo', verbose_name='Logo Brand')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug_dev', models.SlugField(blank=True, null=True, verbose_name='Slug')),
                ('modeldev', models.CharField(blank=True, max_length=20, null=True)),
                ('nameDev', models.CharField(max_length=120, verbose_name='Name')),
                ('networkDev', models.CharField(blank=True, max_length=200, null=True, verbose_name='Network')),
                ('announcedDev', models.CharField(blank=True, max_length=200, null=True, verbose_name='Announced')),
                ('statusDev', models.CharField(blank=True, max_length=200, null=True, verbose_name='Status')),
                ('dimensionsDev', models.CharField(blank=True, max_length=200, null=True, verbose_name='Device Dimensions')),
                ('wightDev', models.CharField(blank=True, max_length=200, null=True, verbose_name='Device Wight')),
                ('buildDev', models.CharField(blank=True, max_length=200, null=True, verbose_name='Build')),
                ('simDev', models.CharField(blank=True, max_length=200, null=True, verbose_name='Sim')),
                ('displayTypeDev', models.CharField(blank=True, max_length=200, null=True, verbose_name='Screen Type')),
                ('displaySizeDev', models.CharField(blank=True, max_length=200, null=True, verbose_name='Screen Size')),
                ('displayResDev', models.CharField(blank=True, max_length=200, null=True, verbose_name='Screen Resolution')),
                ('oSDev', models.CharField(blank=True, max_length=150, null=True, verbose_name='Android')),
                ('chipsetDev', models.CharField(blank=True, max_length=150, null=True, verbose_name='Chipset')),
                ('cPUDev', models.CharField(blank=True, max_length=300, null=True, verbose_name='CPU')),
                ('cardSlotDev', models.CharField(blank=True, max_length=50, null=True, verbose_name='Card Slot')),
                ('internalDev', models.CharField(blank=True, max_length=200, null=True, verbose_name='Device Storage')),
                ('mainCameraDev', models.CharField(blank=True, max_length=300, null=True, verbose_name='Main Camera')),
                ('main_camera_featuresDev', models.CharField(blank=True, max_length=150, null=True, verbose_name='Features Main Camera')),
                ('main_camera_videoDev', models.CharField(blank=True, max_length=150, null=True, verbose_name='Main Camera Video')),
                ('selfieCameraDev', models.CharField(blank=True, max_length=200, null=True, verbose_name='Selfie Camera')),
                ('selfie_camera_videoDev', models.CharField(blank=True, max_length=100, null=True, verbose_name='Selfie Camera Video')),
                ('loudspeakerDev', models.CharField(blank=True, max_length=100, null=True, verbose_name='Loudspeaker')),
                ('wlanDev', models.CharField(blank=True, max_length=100, null=True, verbose_name='WLAN')),
                ('bluetoothDev', models.CharField(blank=True, max_length=100, null=True, verbose_name='Bluetooth')),
                ('nfcDev', models.CharField(blank=True, max_length=100, null=True, verbose_name='NFC')),
                ('radioDev', models.CharField(blank=True, max_length=100, null=True, verbose_name='Radio')),
                ('usbDev', models.CharField(blank=True, max_length=100, null=True, verbose_name='USB')),
                ('sensorsDev', models.CharField(blank=True, max_length=100, null=True, verbose_name='Sensors')),
                ('batteryDev', models.CharField(blank=True, max_length=100, null=True, verbose_name='Battery Type')),
                ('PriceDev', models.CharField(blank=True, max_length=100, null=True, verbose_name='Price')),
                ('imageDev', models.ImageField(blank=True, upload_to='Devices/Devices_Img/', verbose_name='Image Device')),
                ('img_dev_full_1', models.ImageField(blank=True, upload_to='Devices/Devices_full_pic/', verbose_name='Full Image 1 (or front)')),
                ('img_dev_full_2', models.ImageField(blank=True, upload_to='Devices/Devices_full_pic/', verbose_name='Full Image 2 (or back)')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='الاسم الاول')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='اللقب')),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True, verbose_name='رقم التليفون')),
                ('phone_number2', models.CharField(blank=True, max_length=11, null=True, verbose_name='رقم التليفون 2')),
                ('addres', models.CharField(blank=True, max_length=300, null=True, verbose_name='العنوان')),
                ('area', models.CharField(blank=True, max_length=50, null=True, verbose_name='المنقطة')),
                ('mailo', models.EmailField(blank=True, max_length=254, null=True, verbose_name='ايميل (بالشركة)')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Profiles/', verbose_name='صورة شخصية')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='المسمى الوظيفى')),
                ('pos_in_store', models.CharField(blank=True, choices=[('admin', 'Admin'), ('Customer', 'Customer'), ('Tager', 'Tager')], max_length=50, null=True, verbose_name='صفته بالموقع')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='Slug')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='الاسم')),
                ('outlet', models.CharField(blank=True, max_length=50, null=True, verbose_name='منفذ البيع - ')),
                ('the_address', models.CharField(blank=True, max_length=50, null=True, verbose_name='العنوان ')),
                ('region', models.CharField(blank=True, max_length=50, null=True, verbose_name='المنطقة ')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('cute', 'cute'), ('miss ginger', 'miss ginger'), ('for u &  her', 'for u &  her'), ('put ring on it', 'put ring on it'), ('dany', 'dany'), ('angel', 'angel')], max_length=200, null=True, verbose_name='اسم الفرع / المحل')),
                ('location', models.CharField(blank=True, choices=[('cairo', 'cairo'), ('alxandria', 'alxandria'), ('mansoura', 'mansoura'), ('por said', 'por said'), ('october', 'october')], max_length=200, null=True, verbose_name='المكان')),
                ('engineer_name', models.CharField(blank=True, choices=[('ساره', 'ساره'), ('محمد', 'محمد'), ('محمود', 'محمود'), ('احمد', 'احمد'), ('عصام', 'عصام'), ('علي', 'علي'), ('اسماء', 'اسماء'), ('اسراء', 'اسراء'), ('عبدالله', 'عبد الله')], max_length=200, null=True, verbose_name='اسم المهندس')),
                ('category', models.CharField(blank=True, choices=[('cute', 'cute'), ('miss ginger', 'miss ginger'), ('for u &  her', 'for u &  her'), ('put ring on it', 'put ring on it'), ('dany', 'dany'), ('angel', 'angel')], max_length=200, null=True, verbose_name='النوع : التوكيل / المحل')),
                ('brands', models.CharField(blank=True, choices=[('Samsung', 'Samsung'), ('Apple', 'Apple'), ('Huawei', 'Huawei'), ('Oppo', 'Oppo'), ('xiaomi', 'xiaomi'), ('Infinix', 'Infinix'), ('Nokia', 'Nokia'), ('Sony', 'Sony'), ('LG', 'LG'), ('HTC', 'HTC'), ('Lenovo', 'Lenovo'), ('Realme', 'Realme'), ('Honor', 'Honor'), ('ZTE', 'ZTE'), ('Vivo', 'Vivo'), ('Alcatel', 'Alcatel'), ('Asus', 'Asus'), ('Motorola', 'Motorola'), ('Acer', 'Acer'), ('Techno', 'Techno')], max_length=300, null=True, verbose_name='اسم البراند')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='Slug')),
            ],
        ),
        migrations.CreateModel(
            name='Spare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='اسم القطعة')),
                ('fault', models.CharField(blank=True, choices=[(' كسر بالشاشة او التاتش', ' كسر بالشاشة او التاتش'), ('الشاشة او التاتش لا تعمل', 'الشاشة او التاتش لا تعمل'), ('تفريغ سريع فى الشحن', 'تفريغ سريع فى الشحن'), ('لا يظهر علامة الشحن', 'لا يظهر علامة الشحن'), ('علامة الشحن تظهر ولكن الشحن لا يزيد', 'علامة الشحن تظهر ولكن الشحن لا يزيد'), ('الشحن يقل اثناء توصيل الشاحن', 'الشحن يقل اثناء توصيل الشاحن'), ('يظهر علامة التعجب عند الشحن', 'يظهر علامة التعجب عند الشحن'), ('كسر بالشاشة', 'كسر بالشاشة'), ('كسر بالتاتش', 'كسر بالتاتش'), ('كسر بالشاشة والتاتش', 'كسر بالشاشة والتاتش'), ('الشاشة لا تعمل', 'الشاشة لا تعمل'), ('التاتش لا يعمل', 'التاتش لا يعمل'), ('الجهاز لا يعمل', 'الجهاز لا يعمل'), ('لا اسمع صوت الطرف الاخر فى المكالمات', 'لا اسمع صوت الطرف الاخر فى المكالمات'), ('الطرف الاخر فى المكالمات لا يسمعنى', 'الطرف الاخر فى المكالمات لا يسمعنى'), ('الجهاز بيهنج وبطئ فى الاستخدام', 'الجهاز بيهنج وبطئ فى الاستخدام'), ('الجهاز بطئ جدا ويتوقف فجأة عن العمل', 'الجهاز بطئ جدا ويتوقف فجأة عن العمل'), ('الجهاز بيرستر فجأة', 'الجهاز بيرستر فجأة'), ('عطل أخر', 'عطل أخر')], max_length=50, null=True, verbose_name=' العطل الناتج عن تلف القطعة')),
                ('name_to_cstmr', models.CharField(blank=True, choices=[('DisplayScreen', 'DisplayScreen'), ('Lcd', 'Lcd'), ('Touch', 'Touch'), ('Board', 'Board'), ('Mic', 'Mic'), ('LoudSpeaker', 'LoudSpeaker'), ('EarSpeaker', 'EarSpeaker'), ('Ringer', 'Ringer'), ('ChargingJack', 'ChargingJack'), ('Button', 'Button'), ('InternalKeypad', 'InternalKeypad'), ('SubBoard', 'SubBoard'), ('MainCamera', 'MainCamera'), ('SelfieCamera', 'SelfieCamera'), ('Housing', 'Housing'), ('BackCover', 'BackCover'), ('HandfreeJack', 'HandfreeJack'), ('Vibrator', 'Vibrator'), ('Battery', 'Battery'), ('IC-Power', 'IC-Power'), ('IC-Charging', 'IC-Charging'), ('IC-Screendata', 'IC-Screendata'), ('Clean-Parts', 'Clean-Parts'), ('Antenna', 'Antenna'), ('Others', 'Others')], max_length=50, null=True, verbose_name='نوع القطعة')),
                ('quality', models.CharField(blank=True, choices=[('copy', 'copy'), ('highcopy', 'highcopy'), ('original', 'original(new)'), ('original(used)', 'original(used)'), ('original(changeglass)', 'original(changeglass)'), ('other', 'other')], max_length=200, null=True, verbose_name='جودة القطعة')),
                ('quality_degree', models.CharField(blank=True, choices=[('Master', 'Master'), ('TheSame', 'TheSame'), ('Copy', 'Copy')], max_length=20, null=True, verbose_name='درجة الجودة')),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='تكلفة القطعة')),
                ('delivery', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField(verbose_name='السعر')),
                ('price_in_trade_in_offer', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='Slug')),
                ('brand_dev', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Brandspr', to='app.brand', verbose_name='اسم البراند')),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.device', verbose_name='اسم الجهاز')),
                ('stotre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.store')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='اسم الخدمة')),
                ('type', models.CharField(blank=True, max_length=50, null=True, verbose_name='نوع الخدمة')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('fixed_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to='app.profile', verbose_name='العميل (طالب الخدمة)')),
                ('fixed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fixed_by', to='app.profile', verbose_name='التاجر (مقدم الخدمة)')),
                ('mobile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.device')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='stores',
            field=models.ManyToManyField(blank=True, to='app.store', verbose_name='الفروع المسئول عنها'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='السعر')),
                ('accessories', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.accessories')),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.device')),
                ('spare', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.spare')),
            ],
        ),
    ]
