export PROJECT_ID=prj-data-science-sandbox
export REGION=us-west2
export SERVICE_NAME=dry-extrudate

echo "============================"
echo $SERVICE_NAME

docker build $PWD --tag $SERVICE_NAME
echo "======================="
echo "< Docker image built >"
echo "======================="


gcloud builds submit --tag gcr.io/$PROJECT_ID/$SERVICE_NAME --project $PROJECT_ID
echo "================================"
echo "< Image pushed to GCP registry >"
echo "================================"


gcloud run deploy $SERVICE_NAME \
    --image=gcr.io/$PROJECT_ID/$SERVICE_NAME:latest \
    --region $REGION \
    --project $PROJECT_ID
echo "======================================="
echo "< Image deployed to Cloud Run service >"
echo "======================================="