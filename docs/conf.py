#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SimCenter - General documentation build configuration file
#

# -- SimCenter App selection -------------------------------------------------

import os
app_name = os.path.expandvars("$SIMDOC_APP")
if app_name in ["R2DTool", "PBE", "EE-UQ", "WE-UQ", "quoFEM", "pelicun"]:
	pass
else:
	pass
	#app_name = 'R2DTool'
	#app_name = 'PBE'
	#app_name = 'EE-UQ'
	#app_name = 'WE-UQ'
	app_name = 'quoFEM'
	#app_name = 'pelicun'

	os.environ['SIMDOC_APP'] = app_name
	os.environ['SIMCENTER_DEV'] = os.path.normpath('../../')

print('app_name = ' + app_name)


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import sys
sys.path.append(os.path.abspath('./sphinx_ext/'))

if app_name == 'pelicun':
	sys.path.insert(0, os.path.abspath('.'))
	sys.path.insert(0, os.path.abspath('../'))

exclude_patterns = [
		'**/*desktop*',
		'**/*response*',
		'**/*earthquake*',
		'**/*wind*',
		'**/*R2DTool*',
		'**/*PBE*',
		'**/*WEUQ*',
		'**/*WE[-_]UQ*',
		'**/*EEUQ*',
		'**/*EE[-_]UQ*',
		'**/*TinF*',
		'**/*TInF*',
		'**/*pelicun*',
		'**/*old*',
		'**/*quoFEM*',
		'**/qfem*'
	]

source_suffix = {
	".rst": "restructuredtext",
	# ".md" : "markdown"
}

toc_filter_exclusions = [
	'desktop',
	'response',
	'earthquake',
	'wind',
	'R2D',
	'PBE',
	'quoFEM',
	'notQuoFEM',
	'WEUQ',
	'EEUQ',
	'TinF',
	'TInF',
	'S3hark',
	'pelicun'
]
# gallery data sources
rendre_config = {

}

extensions = []

# -- Project information -----------------------------------------------------

# shared among all SimCenter docs

numfig = True
numfig_secnum_depth = 2

math_number_all = True
math_eqref_format = '({number})'
math_numfig = True

rst_prolog = """
.. |EE-UQ short name| replace:: EE-UQ app
.. |EE-UQ app link| replace:: `EE-UQ app`_
.. _EE-UQ app: https://simcenter.designsafe-ci.org/research-tools/ee-uq-application/
.. |user survey link| replace:: `user survey`_
.. _user survey: https://docs.google.com/forms/d/e/1FAIpQLSfh20kBxDmvmHgz9uFwhkospGLCeazZzL770A2GuYZ2KgBZBA/viewform?usp=sf_link
.. |ResearchTools| replace:: `SimCenter Research Tools`_
.. _SimCenter Research Tools: https://simcenter.designsafe-ci.org/research-tools/overview/
.. |OpenSees| replace:: **OpenSees**
.. |userSurveyLink| replace:: `user survey`_
.. |Tcl| replace:: **Tcl**
.. |OpenSeesLink| replace:: `OpenSees`_
.. _OpenSees: https://opensees.berkeley.edu
.. |OpenSeesDownload| replace:: `OpenSees Download`_
.. _OpenSees Download: https://opensees.berkeley.edu/OpenSees/user/download.php
.. |Dakota| replace:: **Dakota**
.. |DakotaLink| replace:: `Dakota`_
.. _Dakota: https://dakota.sandia.gov/
.. |DakotaDownload| replace:: `Dakota Download`_
.. _Dakota Download: https://dakota.sandia.gov/download.html
.. |Dakota Theory Manual| replace:: `Dakota Theory Manual`_
.. _Dakota Theory Manual: https://dakota.sandia.gov/sites/default/files/docs/6.11/Theory-6.11.0.pdf
.. |FEAPpv| replace:: **FEAPpv**
.. |FeapLink| replace:: `FEAPpv`_
.. _FEAPpv: http://projects.ce.berkeley.edu/feap/feappv/
.. |FEAPpvDownload| replace:: `FEAPpv`_
.. |FEAPpv Theory Manual| replace:: `FEAPpv Manual`_
.. _FEAPpv Manual: http://projects.ce.berkeley.edu/feap/feappv/manual_51.pdf
.. |OpenSeesPy| replace:: **OpenSeesPy**

.. |requirements| replace:: **REQUIREMENTS**
.. |DesignSafe| replace:: `DesignSafe`_
.. _DesignSafe: https://designsafe-ci.org
.. |smelt| replace:: `smelt`_
.. _smelt: https://github.com/NHERI-SimCenter/smelt
.. |s3harkName| replace:: *s*\ :sup:`3`\ *hark*
.. |br| raw:: html

    <br>

"""

extlinks = {
}
example_repo = f'https://github.com/NHERI-SimCenter/SimCenterDocumentation/tree/master/docs/common/user_manual/examples/desktop/{app_name.replace("-","")}'

# app-specific settings

if app_name == 'R2DTool':

	project = 'Regional Resilience Determination Tool'
	copyright = '2019, The Regents of the University of California'

	author = 'Adam Zsarnóczay, Frank McKenna, Michael Gardner, Wael Elhaddad, Joanna Zou, Chaofeng Wang'

	tags.add('R2D_app')
	tags.add('desktop_app')
	tags.add('earthquake')
	tags.add('response')
	tags.add('notQuoFEM')

	toc_filter_exclusions.remove('R2D')
	toc_filter_exclusions.remove('desktop')
	toc_filter_exclusions.remove('earthquake')
	toc_filter_exclusions.remove('response')
	toc_filter_exclusions.remove('notQuoFEM')
	toc_filter_exclude = toc_filter_exclusions

	exclude_patterns.remove('**/*desktop*')
	exclude_patterns.remove('**/*earthquake*')
	exclude_patterns.remove('**/*response*')
	exclude_patterns.remove('**/*R2DTool*')

	# TODO: fix these temporary changes
	exclude_patterns.append('**/*architectureLevel4.rst*')
	exclude_patterns.append('**/requirements/index.rst')
	exclude_patterns.append('**/requirements/bigRequirements.rst')
	exclude_patterns.append('**/DakotaSensitivity.rst')
	exclude_patterns.append('**/DakotaReliability.rst')
	exclude_patterns.append('**/DakotaParameterEstimation.rst')
	exclude_patterns.append('**/DakotaInverseProblems.rst')
	exclude_patterns.append('**/resEE.rst')

	# END TODO

	rst_prolog += """\
.. |full tool name| replace:: Regional Resilience Determination Tool
.. |short tool name| replace:: R2D app
.. |short tool id| replace:: R2D
.. |tool github link| replace:: `R2D Github page`_
.. _R2D Github page: https://github.com/NHERI-SimCenter/R2DTool
.. |app| replace:: R2D app
.. |appName| replace:: R2D app
.. |messageBoard| replace:: `Message Board`_
.. _Message Board: https://simcenter-messageboard.designsafe-ci.org/smf/index.php?board=8.0
.. |githubLink| replace:: `R2D Github page`_
.. |appLink| replace:: `R2D Download`_
.. _R2D Download: https://www.designsafe-ci.org/data/browser/public/designsafe.storage.community/%2FSimCenter%2FSoftware%2FRDT
.. |tool version| replace:: 2.0
.. |figDownload| replace:: :numref:`figDownloadR2D`
.. |figUI| replace:: :numref:`figUI-R2D`
.. |figGenericUI| replace:: :numref:`figGenericUI-R2D`
.. |figMissingCRT| replace:: :numref:`figMissingCRT-R2D`
.. |contact person| replace:: Frank McKenna, NHERI SimCenter, UC Berkeley, fmckenna@berkeley.edu
.. |developers| replace:: **SimCenter PI's and Developers**

"""

	# html_logo = 'common/figures/SimCenter_RDT_logo.png'
	html_logo = 'common/figures/RDT-Logo-grey3.png'

	html_theme_options = {
		'analytics_id': '...', #TODO: add analytics ID
		'logo_only': True,
		'prev_next_buttons_location': None,
		'style_nav_header_background': '#F2F2F2'
	}

elif app_name == 'PBE':

	project = 'Performance Based Engineering Application'
	copyright = '2019, The Regents of the University of California'

	author = 'Adam Zsarnóczay, Frank McKenna, Chaofeng Wang, Wael Elhaddad, Michael Gardner'

	tags.add('PBE_app')
	tags.add('desktop_app')
	tags.add('earthquake')
	tags.add('notQuoFEM')

	toc_filter_exclusions.remove('PBE')
	toc_filter_exclusions.remove('desktop')
	toc_filter_exclusions.remove('earthquake')
	toc_filter_exclusions.remove('notQuoFEM')
	toc_filter_exclude = toc_filter_exclusions

	exclude_patterns.remove('**/*desktop*')
	exclude_patterns.remove('**/*earthquake*')
	exclude_patterns.remove('**/*PBE*')

	# TODO: fix these temporary changes
	exclude_patterns.append('**/*architectureLevel4.rst*')
	exclude_patterns.append('**/requirements/index.rst')
	exclude_patterns.append('**/requirements/bigRequirements.rst')
	exclude_patterns.append('**/DakotaSensitivity.rst')
	exclude_patterns.append('**/DakotaReliability.rst')
	exclude_patterns.append('**/DakotaParameterEstimation.rst')
	exclude_patterns.append('**/DakotaInverseProblems.rst')
	exclude_patterns.append('**/resEE.rst')

	# END TODO




	rst_prolog += """\
.. |full tool name| replace:: Performance Based Engineering Application
.. |short tool name| replace:: PBE app
.. |short tool id| replace:: PBE
.. |tool github link| replace:: `PBE Github page`_
.. _PBE Github page: https://github.com/NHERI-SimCenter/PBE
.. |app| replace:: PBE app
.. |appName| replace:: PBE app
.. |messageBoard| replace:: `Message Board`_
.. _Message Board: https://simcenter-messageboard.designsafe-ci.org/smf/index.php?board=7.0
.. |githubLink| replace:: `PBE Github page`_
.. |appLink| replace:: `PBE Download`_
.. _PBE Download: https://www.designsafe-ci.org/data/browser/public/designsafe.storage.community/%2FSimCenter%2FSoftware%2FPBE
.. |tool version| replace:: 2.0
.. |figDownload| replace:: :numref:`figDownloadPBE`
.. |figUI| replace:: :numref:`figUI-PBE`
.. |figGenericUI| replace:: :numref:`figGenericUI-PBE`
.. |figMissingCRT| replace:: :numref:`figMissingCRT-PBE`
.. |contact person| replace:: Adam Zsarnóczay, NHERI SimCenter, Stanford University, adamzs@stanford.edu
.. |developers| replace:: **Adam Zsarnóczay**, **Frank McKenna**, **Chaofeng Wang**, **Wael Elhaddad**, **Michael Gardner**

"""

	# html_logo = 'common/figures/SimCenter_PBE_logo.png'
	html_logo = 'common/figures/PBE-Logo-grey3.png'

	html_theme_options = {
		'analytics_id': 'UA-158130480-3',
		'logo_only': True,
		'prev_next_buttons_location': None,
		'style_nav_header_background': '#F2F2F2'
	}

elif app_name == 'EE-UQ':
	project = 'Earthquake Engineering with Uncertainty Quantification (EE-UQ)'
	copyright = '2019, The Regents of the University of California'
	author = 'Frank McKenna, Wael Elhaddad, Michael Gardner, Chaofeng Wang, Adam Zsarnóczay'

	tags.add('EEUQ_app')
	tags.add('desktop_app')
	tags.add('response')
	tags.add('earthquake')
	tags.add('notQuoFEM')

	toc_filter_exclusions.remove('EEUQ')
	toc_filter_exclusions.remove('desktop')
	toc_filter_exclusions.remove('earthquake')
	toc_filter_exclusions.remove('response')
	toc_filter_exclusions.remove('notQuoFEM')
	toc_filter_exclude = toc_filter_exclusions

	exclude_patterns.remove('**/*EEUQ*')
	exclude_patterns.remove('**/*desktop*')
	exclude_patterns.remove('**/*earthquake*')
	exclude_patterns.remove('**/*response*')
	exclude_patterns.remove('**/*EE[-_]UQ*')

	rst_prolog += """
.. |full tool name| replace:: Earthquake Engineering with Uncertainty Quantification Application (EE-UQ)
.. |short tool name| replace:: EE-UQ app
.. |short tool id| replace:: EE-UQ
.. |tool github link| replace:: `EE-UQ Github page`_
.. _EE-UQ Github page: https://github.com/NHERI-SimCenter/EE-UQ
.. |tool version| replace:: 2.0
.. |app| replace:: EE-UQ app
.. |appName| replace:: EE-UQ app
.. |githubLink| replace:: `EE-UQ Github page`_
.. |appLink| replace:: `EE-UQ Download`_
.. _EE-UQ Download: https://www.designsafe-ci.org/data/browser/public/designsafe.storage.community//SimCenter/Software/EE_UQ
.. |messageBoard| replace:: `Message Board`_
.. _Message Board: https://simcenter-messageboard.designsafe-ci.org/smf/index.php?board=6.0
.. |figUI| replace:: :numref:`figUI-EE`
.. |figDownload| replace:: :numref:`figDownloadEE`
.. |figGenericUI| replace:: :numref:`figGenericUI-EE`
.. |figMissingCRT| replace:: :numref:`figMissingCRT-EE`
.. |contact person| replace:: Frank McKenna, NHERI SimCenter, UC Berkeley, fmckenna@berkeley.edu
.. |developers| replace:: **Frank McKenna**, **Wael Elhaddad**, **Michael Gardner**, **Chaofeng Wang**, **Adam Zsarnóczay**

"""

	html_logo = 'common/figures/EE-UQ-Logo-grey3.png'

	html_theme_options = {
		'analytics_id': 'UA-158130480-1',
		'logo_only': True,
		'prev_next_buttons_location': None,
		'style_nav_header_background': '#F2F2F2'
	}

elif app_name == 'quoFEM':
	project = 'Quantified Uncertainty with Optimization for the FEM'
	copyright = '2018-2020, The Regents of the University of California'
	author = 'Frank McKenna, Adam Zsarnóczay, Nikhil Padhye'

	tags.add('quoFEM_app')
	tags.add('desktop_app')

	toc_filter_exclusions.remove('desktop')
	toc_filter_exclusions.remove('quoFEM')
	toc_filter_exclude = toc_filter_exclusions

	exclude_patterns.remove('**/*desktop*')
	exclude_patterns.remove('**/*quoFEM*')
	exclude_patterns.remove('**/qfem*')

	# TODO: fix these temporary changes
	exclude_patterns.append('**/*architectureLevel4.rst*')
	exclude_patterns.append('**/requirements/index.rst')
	exclude_patterns.append('**/requirements/bigRequirements.rst')
	exclude_patterns.append('**/resEE.rst')
	exclude_patterns.append('**/damping.rst')
	exclude_patterns.append('**/desktop/FEM.rst')
	exclude_patterns.append('**/desktop/GI.rst')
	exclude_patterns.append('**/desktop/SIM.rst')
	# exclude_patterns.append('**/desktop/qfem-*')
	exclude_patterns.append('**/desktop/quo-*')
	exclude_patterns.append('**/testbeds/*')
	# END TODO

	rst_prolog += f"""
.. |full tool name| replace:: Quantified Uncertainty with Optimization for the Finite Element Method (quoFEM)
.. |short tool name| replace:: quoFEM app
.. |short tool id| replace:: quoFEM
.. |tool github link| replace:: `quoFEM Github page`_
.. _quoFEM Github page: https://github.com/NHERI-SimCenter/quoFEM
.. |tool version| replace:: 2.0
.. |app| replace:: quoFEM app
.. |appName| replace:: quoFEM app
.. |githubLink| replace:: `quoFEM Github page`_
.. |appLink| replace:: `quoFEM Download`_
.. _quoFEM Download: https://www.designsafe-ci.org/data/browser/public/designsafe.storage.community//SimCenter/Software/quoFEM
.. |messageBoard| replace:: `Message Board`_
.. _Message Board: https://simcenter-messageboard.designsafe-ci.org/smf/index.php?board=4.0
.. |figUI| replace:: :numref:`figQUO_FEM`
.. |figDownload| replace:: :numref:`figDownloadQUO_FEM`
.. |figGenericUI| replace:: :numref:`figGenericUI-QUOFEM`
.. |figMissingCRT| replace:: :numref:`figMissingCRT-EE`
.. |contact person| replace:: Frank McKenna, NHERI SimCenter, UC Berkeley, fmckenna@berkeley.edu
.. |developers| replace:: {author}"""

	html_logo = 'common/figures/quoFEM-LogoImageGrey-app.png'

	html_theme_options = {
		'analytics_id': 'UA-158130480-4',
		'logo_only': True,
		'prev_next_buttons_location': None,
		'style_nav_header_background': '#F2F2F2'
	}

	# Example links
	extlinks.update(
	   {f'qfem-{i:04}' : (f'{example_repo}/qfem-{i:04}/%s',f'qfem-{i:04}') for i in range(1,99)}
	)

elif app_name == 'WE-UQ':
	project = 'Wind Engineering with Uncertainty Quantification'
	copyright = '2019, The Regents of the University of California'
	author = 'Frank McKenna'

	tags.add('WEUQ_app')
	tags.add('desktop_app')
	tags.add('response')
	tags.add('wind')
	tags.add('notQuoFEM')

	toc_filter_exclusions.remove('WEUQ')
	toc_filter_exclusions.remove('desktop')
	toc_filter_exclusions.remove('wind')
	toc_filter_exclusions.remove('response')
	toc_filter_exclusions.remove('notQuoFEM')
	toc_filter_exclude = toc_filter_exclusions

	exclude_patterns.remove('**/*WEUQ*')
	exclude_patterns.remove('**/*desktop*')
	exclude_patterns.remove('**/*wind*')
	exclude_patterns.remove('**/*response*')
	exclude_patterns.remove('**/*TinF*')
	exclude_patterns.remove('**/*WE[-_]UQ*')

	rst_prolog += """
.. |full tool name| replace:: Wind Engineering with Uncertainty Quantification Application (WE-UQ)
.. |short tool name| replace:: WE-UQ app
.. |short tool id| replace:: WE-UQ
.. |tool github link| replace:: `WE-UQ Github page`_
.. _WE-UQ Github page: https://github.com/NHERI-SimCenter/WE-UQ
.. |tool version| replace:: 2.0
.. |app| replace:: WE-UQ app
.. |appName| replace:: WE-UQ app
.. |githubLink| replace:: `WE-UQ Github page`_
.. |appLink| replace:: `WE-UQ Download`_
.. _WE-UQ Download: https://www.designsafe-ci.org/data/browser/public/designsafe.storage.community//SimCenter/Software/WE_UQ
.. |messageBoard| replace:: `Message Board`_
.. _Message Board: https://simcenter-messageboard.designsafe-ci.org/smf/index.php?board=5.0
.. |figUI| replace:: :numref:`figUI-WE`
.. |figDownload| replace:: :numref:`figDownloadWE`
.. |figGenericUI| replace:: :numref:`figGenericUI-WE`
.. |figMissingCRT| replace:: :numref:`figMissingCRT-WE`
.. |contact person| replace:: Frank McKenna, NHERI SimCenter, UC Berkeley, fmckenna@berkeley.edu
.. |developers| replace:: **Frank McKenna**, **Peter Mackenzie-Helnwein**, **Wael Elhaddad**, **Jiawei Wan**, **Michael Gardner**, **Dae Kun Kwon**


"""

	html_logo = 'common/figures/WE-UQ-Logo-grey3.png' #TODO: replace with EE-UQ logo!


	html_theme_options = {
		'analytics_id': 'UA-158130480-2',
		'logo_only': True,
		'prev_next_buttons_location': None,
		'style_nav_header_background': '#F2F2F2'
	}

	# Example links
	extlinks.update(
	   {f'weuq-{i:02}' : (f'{example_repo}/weuq-{i:02}/%s',f'weuq-{i:02}') for i in range(1,99)}
	)


elif app_name == 'pelicun':

	project = 'pelicun'
	copyright = '(c) 2018-2020, Leland Stanford Junior University and The Regents of the University of California'
	author = 'Adam Zsarnóczay'

	tags.add('pelicun')

	toc_filter_exclusions.remove('pelicun')
	toc_filter_exclude = toc_filter_exclusions

	exclude_patterns.remove('**/*pelicun*')

	rst_prolog += """\
.. |pelicun expanded| replace:: Probabilistic Estimation of Losses, Injuries, and Community resilience Under Natural disasters
.. |full tool name| replace:: pelicun library
.. |short tool name| replace:: pelicun
.. |short tool id| replace:: pelicun
.. |tool github link| replace:: `pelicun Github page`_
.. _pelicun Github page: https://github.com/NHERI-SimCenter/pelicun
.. |app| replace:: pelicun library
.. |messageBoard| replace:: `Message Board`_
.. _Message Board: https://simcenter-messageboard.designsafe-ci.org/smf/index.php?board=7.0
.. |githubLink| replace:: `pelicun Github page`_
.. |tool version| replace:: 2.0.9
.. |contact person| replace:: Adam Zsarnóczay, NHERI SimCenter, Stanford University, adamzs@stanford.edu
.. |developers| replace:: **Adam Zsarnóczay**
"""

	extensions = [
	    'sphinx.ext.autodoc',
	    'sphinx.ext.todo',
	    'sphinx.ext.mathjax',
	    'sphinx.ext.viewcode',
	    'sphinx.ext.githubpages',
	    'numpydoc',
	    'sphinx.ext.autosummary',
	    'sphinx.ext.intersphinx',
	    'sphinx.ext.coverage',
	    'sphinx.ext.doctest'
	]

	numpydoc_show_class_members = True
	numpydoc_class_members_toctree = False
	autodoc_member_order = 'bysource'
	autoclass_content = 'both'

	import glob
	autosummary_generate = glob.glob("source/*.rst")

	master_doc = 'index'

	language = None

	pygments_style = 'sphinx'

	html_logo = 'common/figures/pelicun-Logo-grey3.png'

	html_theme_options = {
		'analytics_id': 'UA-158130480-7',
		'logo_only': True,
		'prev_next_buttons_location': None,
		'style_nav_header_background': '#F2F2F2'
	}

	htmlhelp_basename = 'pelicundoc'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = extensions + [
    'sphinx-jsonschema',
    'sphinxcontrib.bibtex',
    'toctree_filter',
    'sphinxcontrib.images',
	'sphinx.ext.extlinks',
	'sphinxcontrib.images',
	'rendre.sphinx'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = (exclude_patterns +
					['_build', 'Thumbs.db', '.DS_Store', '_archive'])

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

#html_theme_options = {'body_max_width': '70%'}

#	'style_nav_header_background': '#F2F2F2'
#	'style_nav_header_background': '#FFFFFF'
#	'style_nav_header_background': '#d5d5d5'
#
#	'style_nav_header_background': '#F2F2F2' #64B5F6 #607D8B

html_css_files = [
	'css/custom.css'
]

html_secnum_suffix = " "

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static','_static/css/']

# For a full list of configuration options see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

#latex_docclass = {
#	r'manual': 'simcenterdocumentation',
#	r'howto': 'simcenterdocumentation'
#}

latex_elements = {
  'extraclassoptions': 'openany,oneside'
}
latex_documents = [
	(
		'index',
		app_name + ".tex", # tex output file
		project,          # Document title
		author.replace(', ',' \\and '), # authors
		'manual'           # latex theme
	)
]
latex_logo = 'common/figures/NSF_SimCenter_NO TEXT_SimCenter.png'
