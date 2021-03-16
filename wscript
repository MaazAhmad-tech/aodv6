# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

# def options(opt):
#     pass

# def configure(conf):
#     conf.check_nonfatal(header_name='stdint.h', define_name='HAVE_STDINT_H')

def build(bld):
    module = bld.create_ns3_module('aodv6', ['core'])
    module.source = [
        'model/aodv6.cc',
        'helper/aodv6-helper.cc',
        ]

    module_test = bld.create_ns3_module_test_library('aodv6')
    module_test.source = [
        'test/aodv6-test-suite.cc',
        ]
    # Tests encapsulating example programs should be listed here
    if (bld.env['ENABLE_EXAMPLES']):
        module_test.source.extend([
        #    'test/aodv6-examples-test-suite.cc',
             ])

    headers = bld(features='ns3header')
    headers.module = 'aodv6'
    headers.source = [
        'model/aodv6.h',
        'helper/aodv6-helper.h',
        ]

    if bld.env.ENABLE_EXAMPLES:
        bld.recurse('examples')

    # bld.ns3_python_bindings()

