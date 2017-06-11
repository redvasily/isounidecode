# -*- coding: utf8 -*-
import sys
from .codes import codes

if sys.version_info[0] >= 3:
    unichr = chr

def build_8859_translation(codes):
    codes_8859 = {}

    for code in codes:
        translation = codes[code]
        tr_8859 = translation
        try:
            tr_8859 = unichr(code).encode('iso-8859-1')
        except UnicodeEncodeError:
            pass
        codes_8859[code] = tr_8859

    # Dannish fixes
    codes_8859[ord(u'Ĳ')] = b'IJ'
    codes_8859[ord(u'ĳ')] = b'ij'

    # Estonian fixes
    codes_8859[ord(u'Š')] = b'S'
    codes_8859[ord(u'š')] = b's'
    codes_8859[ord(u'Ž')] = b'Z'
    codes_8859[ord(u'ž')] = b'z'

    # French fixes
    codes_8859[ord(u'Œ')] = b'OE'
    codes_8859[ord(u'œ')] = b'oe'
    codes_8859[ord(u'Ÿ')] = b'Y'
    codes_8859[ord(u'ÿ')] = b'y'

    # Finnish fixes
    codes_8859[ord(u'Š')] = b'S'
    codes_8859[ord(u'š')] = b's'
    codes_8859[ord(u'Ž')] = b'Z'
    codes_8859[ord(u'ž')] = b'z'

    return codes_8859

codes_8859 = build_8859_translation(codes)

translations = {
    'ascii': codes,
    'iso8859-1': codes_8859}

def unidecode(u, translation='ascii'):
    return b''.join(translations[translation].get(ord(c), b'') for c in u)

