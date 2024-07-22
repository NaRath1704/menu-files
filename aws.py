import boto3

def launch_ec2_instance():
    # Create a session using boto3
    session = boto3.Session(
    aws_access_key_id=',
    aws_secret_access_key='
    region_name='ap-south-1'  # Replace with your desired region
    )   

    # Use the session to create an EC2 resource
    ec2 = session.resource('ec2')

    # Launch the EC2 instance
    instances = ec2.create_instances(
        ImageId='ami-0ec0e125bb6c6e8ec',  # Replace with a valid AMI ID
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',  # Replace with the desired instance type
        SecurityGroupIds=['sg-0626809b2ee8efe6d'],  # Replace with your security group ID
    )
    # Print the ID of the new instance
    for instance in instances:
        print("Instance ID:", instance.id)

if __name__ == '__main__':
    launch_ec2_instance()

