# fasttext-server

Flask web server to serve supervised models trained with FastText.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You'll need [python](http://docs.python-guide.org/en/latest/starting/installation/) + [pipenv](https://docs.pipenv.org/) installed.

### Installing & Running

* Clone the repository
* Run `pipenv install`
* Fill the config_tmpl.py file with your parameters and rename it to config.py
* Run `python app.py`

## Deployment

Coming soon!

## Built With

* [flask](http://flask.pocoo.org/) - Python web framework
* [pyfasttext](https://github.com/vrasneur/pyfasttext) - Python bindings for FastText (which does all the actual work)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
