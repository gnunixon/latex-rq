from rq.decorators import job
from redis import StrictRedis
from subprocess import Popen
from base64 import b64encode
import os
from glob import glob


@job('normal', connection=redis_conn, timeout=5)
def compile(latex_file, latex_class_name='', latex_class=''):
    ret = None
    if latex_class_name and latex_class:
        f = open(latex_class_name, 'w')
        f.write(latex_class)
        f.close()
    if not latex_file:
        return
    f = open('latex.tex', 'w')
    f.write(latex_file)
    f.close()
    p = Popen("pdflatex latex.tex", stdout=compile_out, stderr=compile_err)
    if not compile_err:
        f = open('latex.pdf', 'r')
        content = f.read()
        ret = b64encode(content)
    os.remove(glob('latex.*'))
    return ret
