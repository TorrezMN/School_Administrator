

echo "========================"
echo "Refresh static files."
echo "========================"

# echo $PWD

python3 SChool_Admin_App/manage.py collectstatic --noinput
