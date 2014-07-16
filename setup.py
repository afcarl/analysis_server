#
# This file is autogenerated during plugin quickstart and overwritten during
# plugin makedist. DO NOT CHANGE IT if you plan to use plugin makedist to update 
# the distribution.
#

from setuptools import setup, find_packages

kwargs = {'author': '',
 'author_email': '',
 'classifiers': ['Intended Audience :: Science/Research',
                 'Topic :: Scientific/Engineering'],
 'description': "OpenMDAO interface to Phoenix Integration's ModelCenter/AnalysisServer",
 'download_url': '',
 'entry_points': '[openmdao.variable]\nanalysis_server.proxy.EnumProxy=analysis_server.proxy:EnumProxy\nanalysis_server.proxy.ListProxy=analysis_server.proxy:ListProxy\nanalysis_server.proxy.BoolProxy=analysis_server.proxy:BoolProxy\nanalysis_server.proxy.IntProxy=analysis_server.proxy:IntProxy\nanalysis_server.proxy.StrProxy=analysis_server.proxy:StrProxy\nanalysis_server.proxy.ArrayProxy=analysis_server.proxy:ArrayProxy\nanalysis_server.proxy.FloatProxy=analysis_server.proxy:FloatProxy\nanalysis_server.proxy.FileProxy=analysis_server.proxy:FileProxy\n\n[openmdao.component]\nanalysis_server.test.OptComps.RosenSuzuki.RosenSuzuki=analysis_server.test.OptComps.RosenSuzuki:RosenSuzuki\nASTestComp.TestComponent=ASTestComp:TestComponent\nanalysis_server.proxy.ComponentProxy=analysis_server.proxy:ComponentProxy\nanalysis_server.test.ASTestComp.TestComponent=analysis_server.test.ASTestComp:TestComponent\nanalysis_server.test.test_proxy.Sink=analysis_server.test.test_proxy:Sink\nanalysis_server.test.OptComps.RosenSuzuki.PrintEnvironment=analysis_server.test.OptComps.RosenSuzuki:PrintEnvironment\nanalysis_server.test.test_proxy.Source=analysis_server.test.test_proxy:Source\nanalysis_server.test.test_proxy.Model=analysis_server.test.test_proxy:Model\n\n[openmdao.container]\nanalysis_server.proxy.ObjProxy=analysis_server.proxy:ObjProxy\nanalysis_server.test.test_proxy.Sink=analysis_server.test.test_proxy:Sink\nASTestComp.SubObj=ASTestComp:SubObj\nASTestComp.TestComponent=ASTestComp:TestComponent\nanalysis_server.proxy.ComponentProxy=analysis_server.proxy:ComponentProxy\nASTestComp.SubGroup=ASTestComp:SubGroup\nanalysis_server.test.ASTestComp.SubObj=analysis_server.test.ASTestComp:SubObj\nanalysis_server.test.test_proxy.Model=analysis_server.test.test_proxy:Model\nanalysis_server.test.OptComps.RosenSuzuki.RosenSuzuki=analysis_server.test.OptComps.RosenSuzuki:RosenSuzuki\nanalysis_server.test.ASTestComp.SubGroup=analysis_server.test.ASTestComp:SubGroup\nanalysis_server.test.ASTestComp.TestComponent=analysis_server.test.ASTestComp:TestComponent\nanalysis_server.test.OptComps.RosenSuzuki.PrintEnvironment=analysis_server.test.OptComps.RosenSuzuki:PrintEnvironment\nanalysis_server.test.ASTestComp.TopObj=analysis_server.test.ASTestComp:TopObj\nanalysis_server.test.test_proxy.Source=analysis_server.test.test_proxy:Source\nASTestComp.TopObj=ASTestComp:TopObj',
 'include_package_data': True,
 'install_requires': ['openmdao.main'],
 'keywords': ['openmdao'],
 'license': '',
 'maintainer': '',
 'maintainer_email': '',
 'name': 'analysis_server',
 'package_data': {'analysis_server': ['sphinx_build/html/index.html',
                                      'sphinx_build/html/.buildinfo',
                                      'sphinx_build/html/py-modindex.html',
                                      'sphinx_build/html/objects.inv',
                                      'sphinx_build/html/searchindex.js',
                                      'sphinx_build/html/search.html',
                                      'sphinx_build/html/pkgdocs.html',
                                      'sphinx_build/html/usage.html',
                                      'sphinx_build/html/genindex.html',
                                      'sphinx_build/html/srcdocs.html',
                                      'sphinx_build/html/_sources/usage.txt',
                                      'sphinx_build/html/_sources/pkgdocs.txt',
                                      'sphinx_build/html/_sources/index.txt',
                                      'sphinx_build/html/_sources/srcdocs.txt',
                                      'sphinx_build/html/_static/plus.png',
                                      'sphinx_build/html/_static/comment-bright.png',
                                      'sphinx_build/html/_static/comment.png',
                                      'sphinx_build/html/_static/down-pressed.png',
                                      'sphinx_build/html/_static/sidebar.js',
                                      'sphinx_build/html/_static/doctools.js',
                                      'sphinx_build/html/_static/ajax-loader.gif',
                                      'sphinx_build/html/_static/default.css',
                                      'sphinx_build/html/_static/down.png',
                                      'sphinx_build/html/_static/jquery.js',
                                      'sphinx_build/html/_static/underscore.js',
                                      'sphinx_build/html/_static/minus.png',
                                      'sphinx_build/html/_static/up-pressed.png',
                                      'sphinx_build/html/_static/up.png',
                                      'sphinx_build/html/_static/pygments.css',
                                      'sphinx_build/html/_static/searchtools.js',
                                      'sphinx_build/html/_static/file.png',
                                      'sphinx_build/html/_static/basic.css',
                                      'sphinx_build/html/_static/websupport.js',
                                      'sphinx_build/html/_static/comment-close.png',
                                      'sphinx_build/html/_modules/index.html',
                                      'sphinx_build/html/_modules/analysis_server/monitor.html',
                                      'sphinx_build/html/_modules/analysis_server/factory.html',
                                      'sphinx_build/html/_modules/analysis_server/server.html',
                                      'sphinx_build/html/_modules/analysis_server/proxy.html',
                                      'sphinx_build/html/_modules/analysis_server/objxml.html',
                                      'sphinx_build/html/_modules/analysis_server/client.html',
                                      'sphinx_build/html/_modules/analysis_server/stream.html',
                                      'sphinx_build/html/_modules/analysis_server/publish.html',
                                      'sphinx_build/html/_modules/analysis_server/mixin.html',
                                      'sphinx_build/html/_modules/analysis_server/sniffer.html',
                                      'sphinx_build/html/_modules/analysis_server/units.html',
                                      'sphinx_build/html/_modules/analysis_server/wrapper.html',
                                      'sphinx_build/html/_modules/analysis_server/test/test_client.html',
                                      'sphinx_build/html/_modules/analysis_server/test/test_proxy.html',
                                      'sphinx_build/html/_modules/analysis_server/test/test_server.html',
                                      'sphinx_build/html/_modules/analysis_server/test/ASTestComp.html',
                                      'sphinx_build/html/_modules/analysis_server/test/OptComps/RosenSuzuki.html',
                                      'test/test.tee',
                                      'test/get_hierarchy64.txt',
                                      'test/__init__.py',
                                      'test/test_client.py',
                                      'test/get_hierarchy32.txt',
                                      'test/test_server.py',
                                      'test/ASTestComp-0.2.cfg',
                                      'test/list_values64.txt',
                                      'test/ASTestComp-0.1.cfg',
                                      'test/ASTestComp2-0.1.cfg',
                                      'test/test_proxy.py',
                                      'test/openmdao_log.txt',
                                      'test/list_values32.txt',
                                      'test/ASTestComp.py',
                                      'test/OptComps/__init__.py',
                                      'test/OptComps/RosenSuzuki.py',
                                      'test/OptComps/RosenSuzuki.cfg',
                                      'test/OptComps/pleiades',
                                      'test/OptComps/PrintEnv.cfg']},
 'package_dir': {'': 'src'},
 'packages': ['analysis_server',
              'analysis_server.test',
              'analysis_server.test.OptComps'],
 'url': '',
 'version': '0.7',
 'zip_safe': False}


setup(**kwargs)

