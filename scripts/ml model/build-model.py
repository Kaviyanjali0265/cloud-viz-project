
import sagemaker 
from sagemaker.amazon.amazon_estimator import get_image_uri 
from sagemaker import get_execution_role

key = 'model/xgb_model'
s3_output_location = url= 's3://{}/{}'.format(bucket_name, key)

xgb_model=sagemaker.estimator.Estimator( 
    get_image_uri(boto3.Session().region_name, 'xgboost'),
    get_execution_role(), 
    train_instance_count= 1,
    train_instance_type='ml.m4.xlarge',
    train_volume_size=5,
    output_path = s3_output_location,
    sagemaker_session=sagemaker.Session()
)

xgb_model.set_hyperparameters(max_depth=5,
                              eta=0.2,
                              gamma=4,
                              min_child_weight=6,
                              silent=0,
                              objective='multi:softmax',
                              num_class=3,
                              num_round=10)
