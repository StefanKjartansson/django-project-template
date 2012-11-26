all: clean flake test

flake:
	flake8 {{ project_name }} || exit 1

test:
	python manage.py --settings={{ project_name }}.test_settings test

clean:  
	find {{ project_name }} -iname "*.pyc"|xargs rm -f 
