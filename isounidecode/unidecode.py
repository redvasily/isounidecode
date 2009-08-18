# -*- coding: utf8 -*-

from codes import codes


def build_8859_translation(codes):
    codes_8859 = {}

    for code, translation in codes.iteritems():
        tr_8859 = translation
        try:
            tr_8859 = unichr(code).encode('iso-8859-1')
        except UnicodeEncodeError:
            pass
        codes_8859[code] = tr_8859

    # Dannish fixes
    codes_8859[ord(u'Ĳ')] = 'IJ'
    codes_8859[ord(u'ĳ')] = 'ij'

    # Estonian fixes
    codes_8859[ord(u'Š')] = 'S'
    codes_8859[ord(u'š')] = 's'
    codes_8859[ord(u'Ž')] = 'Z'
    codes_8859[ord(u'ž')] = 'z'

    # French fixes
    codes_8859[ord(u'Œ')] = 'OE'
    codes_8859[ord(u'œ')] = 'oe'
    codes_8859[ord(u'Ÿ')] = 'Y'
    codes_8859[ord(u'ÿ')] = 'y'

    # Finnish fixes
    codes_8859[ord(u'Š')] = 'S'
    codes_8859[ord(u'š')] = 's'
    codes_8859[ord(u'Ž')] = 'Z'
    codes_8859[ord(u'ž')] = 'z'

    return codes_8859

codes_8859 = build_8859_translation(codes)

translations = {
    'ascii': codes,
    'iso8859-1': codes_8859}

def unidecode(u, translation='ascii'):
    return ''.join(translations[translation].get(ord(c), '') for c in u)

