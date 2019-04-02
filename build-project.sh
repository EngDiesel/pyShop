echo "Generating ../static/ folder"
cp -r static/ ../static/
echo "Please Enter 'yes' to collect static files"
python2 manage.py collectstatic
echo 'Installing requirements, this may take sevral minutes.'
pip install -r requirements.txt