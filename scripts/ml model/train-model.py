train_data = 's3://{}/{}'.format(bucket_name,'data/train')
val_data = 's3://{}/{}'.format(bucket_name,'data/val')

train_channel = sagemaker.session.s3_input(train_data,content_type='text/csv')
val_channel = sagemaker.session.s3_input(val_data,content_type='text/csv')

#dict data_channels with two keys
data_channels = {'train':train_channel,'validation':val_channel}

xgb_model.fit(inputs = data_channels)
