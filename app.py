from uikit.renderer import *


@view
def home():
    return render_template('index.html', title='Home')
