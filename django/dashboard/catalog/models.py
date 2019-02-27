from django.db import models


class ProcessorAdFoundWatchlog(models.Model):
    attempt = models.IntegerField()
    request_timestamp = models.BigIntegerField()
    ad_source = models.CharField(max_length=50)
    ad_duration = models.IntegerField()
    ad_skip_duration = models.IntegerField()
    ad_system = models.CharField(max_length=255)
    ad_video = models.ForeignKey('ProcessorVideo', models.DO_NOTHING)
    batch = models.ForeignKey('ProcessorBatch', models.DO_NOTHING)
    bot = models.ForeignKey('ProcessorBot', models.DO_NOTHING)
    #video_watched = models.ForeignKey('ProcessorVideo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'processor_ad_found_watchlog'


class ProcessorBatch(models.Model):
    start_timestamp = models.BigIntegerField()
    completed_timestamp = models.BigIntegerField()
    time_taken = models.IntegerField()
    total_bots = models.IntegerField()
    server_hostname = models.CharField(max_length=30)
    server_container = models.CharField(max_length=30)
    external_ip = models.CharField(max_length=30)
    status = models.CharField(max_length=20)
    synced = models.IntegerField()
    processed = models.IntegerField()
    total_requests = models.IntegerField()
    total_ads_found = models.IntegerField()
    video_list_size = models.IntegerField()
    remarks = models.CharField(max_length=255)
    location = models.ForeignKey('ProcessorLocation', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'processor_batch'


class ProcessorBot(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'processor_bots'


class ProcessorCategory(models.Model):
    cat_id = models.IntegerField()
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'processor_categories'


class ProcessorChannel(models.Model):
    channel_id = models.TextField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'processor_channels'


class ProcessorLocation(models.Model):
    state_name = models.CharField(max_length=100)
    state_symbol = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'processor_locations'

class ProcessorVideo(models.Model):
    url = models.TextField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.TextField()
    watched_as_ad = models.IntegerField()
    watched_as_video = models.IntegerField()
    category = models.ForeignKey(ProcessorCategory, models.DO_NOTHING)
    channel = models.ForeignKey(ProcessorChannel, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'processor_videos'

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('processorvideo-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.title[:80]

class CustomVideoGroup(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the custom group')
    videos = models.ManyToManyField(ProcessorVideo, help_text='Select videos to be added to this custom group')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('processorvideo-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class PolitcalAdDataByDate(models.Model):
    url = models.TextField()
    batch_startime = models.DateField(blank=True, null=True)
    times_encountered = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'politcal_ad_data_by_date'
