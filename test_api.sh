#!/bin/bash
echo "🔐 Logging in..."
# this test script is only used initailly for testing the db.
LOGIN_RESPONSE=$(curl -s -X POST "http://localhost:8000/auth/login" \
-H "Content-Type: application/json" \
-d '{"username":"teacher1","password":"admin123"}')

echo "Login Response:"
echo "$LOGIN_RESPONSE" | jq

TOKEN=$(echo "$LOGIN_RESPONSE" | jq -r '.access_token')

if [ "$TOKEN" == "null" ] || [ -z "$TOKEN" ]; then
  echo "❌ Failed to get token. Exiting..."
  exit 1
fi

echo "✅ Token received"
echo "$TOKEN"

echo ""
echo "📥 Adding grade..."

ADD_RESPONSE=$(curl -s -X POST "http://127.0.0.1:8000/grades/" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $TOKEN" \
-d '{"name": "Nidhi","student_class": "10A","subject_marks":{"Math": 92,"Science": 88,"English": 90,"IT": 96}}')

echo "Add Grade Response:"
echo $ADD_RESPONSE | jq

echo ""
echo "📊 Fetching grades..."

GET_RESPONSE=$(curl -s -X GET "http://127.0.0.1:8000/grades/" \
-H "Authorization: Bearer $TOKEN")

echo "Grades:"
echo $GET_RESPONSE | jq

echo ""
echo "🎉 Test flow completed!"