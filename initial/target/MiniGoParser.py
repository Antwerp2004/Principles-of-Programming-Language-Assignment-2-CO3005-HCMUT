# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u0250\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\3\2\6\2\u0080\n\2\r\2\16\2\u0081")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u008c\n\3\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u0098\n\4\3\5\3\5")
        buf.write("\6\5\u009c\n\5\r\5\16\5\u009d\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\5\6\u00ab\n\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\5\t\u00bd")
        buf.write("\n\t\3\n\3\n\3\n\5\n\u00c2\n\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\7\f\u00ce\n\f\f\f\16\f\u00d1\13")
        buf.write("\f\3\r\3\r\3\r\3\16\3\16\3\16\5\16\u00d9\n\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\5\21\u00f3\n\21\3\21\3\21\5\21\u00f7\n\21\3\22\3\22\3")
        buf.write("\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\5\26\u010f")
        buf.write("\n\26\3\26\3\26\3\27\3\27\5\27\u0115\n\27\3\27\3\27\3")
        buf.write("\30\3\30\3\30\3\30\5\30\u011d\n\30\3\30\3\30\5\30\u0121")
        buf.write("\n\30\3\30\3\30\3\30\3\31\3\31\3\31\5\31\u0129\n\31\3")
        buf.write("\31\3\31\3\32\3\32\3\32\7\32\u0130\n\32\f\32\16\32\u0133")
        buf.write("\13\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u013d")
        buf.write("\n\33\3\33\3\33\5\33\u0141\n\33\3\33\3\33\3\33\3\34\3")
        buf.write("\34\3\34\3\34\3\35\3\35\3\36\3\36\3\36\5\36\u014f\n\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u0157\n\37\f\37\16")
        buf.write("\37\u015a\13\37\3 \3 \3 \3 \3 \3 \7 \u0162\n \f \16 \u0165")
        buf.write("\13 \3!\3!\3!\3!\3!\3!\3!\7!\u016e\n!\f!\16!\u0171\13")
        buf.write("!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\7\"\u017a\n\"\f\"\16\"\u017d")
        buf.write("\13\"\3#\3#\3#\3#\3#\3#\3#\7#\u0186\n#\f#\16#\u0189\13")
        buf.write("#\3$\3$\3$\5$\u018e\n$\3%\3%\3%\3%\5%\u0194\n%\3&\3&\3")
        buf.write("&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u01a4")
        buf.write("\n\'\3(\3(\3(\3(\3(\3(\5(\u01ac\n(\5(\u01ae\n(\3)\3)\3")
        buf.write(")\3)\3*\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3,\7,\u01c0\n,\f")
        buf.write(",\16,\u01c3\13,\3-\3-\3-\3-\3-\3-\3-\3-\5-\u01cd\n-\3")
        buf.write(".\3.\3.\3.\3/\3/\3/\3/\3/\5/\u01d8\n/\3/\6/\u01db\n/\r")
        buf.write("/\16/\u01dc\3/\3/\6/\u01e1\n/\r/\16/\u01e2\5/\u01e5\n")
        buf.write("/\3\60\3\60\3\60\3\60\3\60\6\60\u01ec\n\60\r\60\16\60")
        buf.write("\u01ed\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\62\3\62\3")
        buf.write("\62\5\62\u01fa\n\62\3\62\3\62\3\63\3\63\3\63\7\63\u0201")
        buf.write("\n\63\f\63\16\63\u0204\13\63\3\64\3\64\3\64\3\64\3\65")
        buf.write("\3\65\3\65\3\65\3\66\3\66\3\66\3\66\6\66\u0212\n\66\r")
        buf.write("\66\16\66\u0213\3\66\3\66\7\66\u0218\n\66\f\66\16\66\u021b")
        buf.write("\13\66\3\67\3\67\3\67\3\67\3\67\6\67\u0222\n\67\r\67\16")
        buf.write("\67\u0223\3\67\3\67\3\67\38\38\38\58\u022c\n8\38\38\5")
        buf.write("8\u0230\n8\38\38\39\39\39\79\u0237\n9\f9\169\u023a\13")
        buf.write("9\3:\3:\3:\7:\u023f\n:\f:\16:\u0242\13:\3:\3:\3;\3;\3")
        buf.write("<\3<\3=\3=\3>\3>\3?\3?\3?\2\7<>@BD@\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRTVXZ\\^`bdfhjlnprtvxz|\2\n\3\2\r\20\4\2\27\27##\4\2")
        buf.write("\65\65@@\3\2\30\32\3\2\26\27\3\2\33 \3\2$)\3\2\3\4\2\u0261")
        buf.write("\2\177\3\2\2\2\4\u008b\3\2\2\2\6\u0097\3\2\2\2\b\u0099")
        buf.write("\3\2\2\2\n\u00a1\3\2\2\2\f\u00ae\3\2\2\2\16\u00b4\3\2")
        buf.write("\2\2\20\u00bc\3\2\2\2\22\u00be\3\2\2\2\24\u00c5\3\2\2")
        buf.write("\2\26\u00cf\3\2\2\2\30\u00d2\3\2\2\2\32\u00d8\3\2\2\2")
        buf.write("\34\u00da\3\2\2\2\36\u00df\3\2\2\2 \u00f6\3\2\2\2\"\u00f8")
        buf.write("\3\2\2\2$\u00fc\3\2\2\2&\u0106\3\2\2\2(\u0109\3\2\2\2")
        buf.write("*\u010e\3\2\2\2,\u0112\3\2\2\2.\u0118\3\2\2\2\60\u0125")
        buf.write("\3\2\2\2\62\u012c\3\2\2\2\64\u0134\3\2\2\2\66\u0145\3")
        buf.write("\2\2\28\u0149\3\2\2\2:\u014e\3\2\2\2<\u0150\3\2\2\2>\u015b")
        buf.write("\3\2\2\2@\u0166\3\2\2\2B\u0172\3\2\2\2D\u017e\3\2\2\2")
        buf.write("F\u018d\3\2\2\2H\u0193\3\2\2\2J\u0195\3\2\2\2L\u01a3\3")
        buf.write("\2\2\2N\u01ad\3\2\2\2P\u01af\3\2\2\2R\u01b3\3\2\2\2T\u01b7")
        buf.write("\3\2\2\2V\u01bc\3\2\2\2X\u01cc\3\2\2\2Z\u01ce\3\2\2\2")
        buf.write("\\\u01e4\3\2\2\2^\u01e6\3\2\2\2`\u01f2\3\2\2\2b\u01f6")
        buf.write("\3\2\2\2d\u01fd\3\2\2\2f\u0205\3\2\2\2h\u0209\3\2\2\2")
        buf.write("j\u020d\3\2\2\2l\u021c\3\2\2\2n\u0228\3\2\2\2p\u0233\3")
        buf.write("\2\2\2r\u023b\3\2\2\2t\u0245\3\2\2\2v\u0247\3\2\2\2x\u0249")
        buf.write("\3\2\2\2z\u024b\3\2\2\2|\u024d\3\2\2\2~\u0080\5\4\3\2")
        buf.write("\177~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\177\3\2\2\2\u0081")
        buf.write("\u0082\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0084\7\2\2\3")
        buf.write("\u0084\3\3\2\2\2\u0085\u008c\5\n\6\2\u0086\u008c\5\f\7")
        buf.write("\2\u0087\u008c\5^\60\2\u0088\u008c\5l\67\2\u0089\u008c")
        buf.write("\5.\30\2\u008a\u008c\5\64\33\2\u008b\u0085\3\2\2\2\u008b")
        buf.write("\u0086\3\2\2\2\u008b\u0087\3\2\2\2\u008b\u0088\3\2\2\2")
        buf.write("\u008b\u0089\3\2\2\2\u008b\u008a\3\2\2\2\u008c\5\3\2\2")
        buf.write("\2\u008d\u0098\5\n\6\2\u008e\u0098\5\f\7\2\u008f\u0098")
        buf.write("\5\16\b\2\u0090\u0098\5\22\n\2\u0091\u0098\5\32\16\2\u0092")
        buf.write("\u0098\5&\24\2\u0093\u0098\5(\25\2\u0094\u0098\5*\26\2")
        buf.write("\u0095\u0098\5,\27\2\u0096\u0098\5|?\2\u0097\u008d\3\2")
        buf.write("\2\2\u0097\u008e\3\2\2\2\u0097\u008f\3\2\2\2\u0097\u0090")
        buf.write("\3\2\2\2\u0097\u0091\3\2\2\2\u0097\u0092\3\2\2\2\u0097")
        buf.write("\u0093\3\2\2\2\u0097\u0094\3\2\2\2\u0097\u0095\3\2\2\2")
        buf.write("\u0097\u0096\3\2\2\2\u0098\7\3\2\2\2\u0099\u009b\7\60")
        buf.write("\2\2\u009a\u009c\5\6\4\2\u009b\u009a\3\2\2\2\u009c\u009d")
        buf.write("\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009e\3\2\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f\u00a0\7\61\2\2\u00a0\t\3\2\2\2\u00a1")
        buf.write("\u00a2\7\22\2\2\u00a2\u00aa\7@\2\2\u00a3\u00ab\5:\36\2")
        buf.write("\u00a4\u00a5\7*\2\2\u00a5\u00ab\5<\37\2\u00a6\u00a7\5")
        buf.write(":\36\2\u00a7\u00a8\7*\2\2\u00a8\u00a9\5<\37\2\u00a9\u00ab")
        buf.write("\3\2\2\2\u00aa\u00a3\3\2\2\2\u00aa\u00a4\3\2\2\2\u00aa")
        buf.write("\u00a6\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad\7\63\2")
        buf.write("\2\u00ad\13\3\2\2\2\u00ae\u00af\7\21\2\2\u00af\u00b0\7")
        buf.write("@\2\2\u00b0\u00b1\7*\2\2\u00b1\u00b2\5<\37\2\u00b2\u00b3")
        buf.write("\7\63\2\2\u00b3\r\3\2\2\2\u00b4\u00b5\5\20\t\2\u00b5\u00b6")
        buf.write("\5z>\2\u00b6\u00b7\5<\37\2\u00b7\u00b8\7\63\2\2\u00b8")
        buf.write("\17\3\2\2\2\u00b9\u00bd\7@\2\2\u00ba\u00bd\5h\65\2\u00bb")
        buf.write("\u00bd\5\\/\2\u00bc\u00b9\3\2\2\2\u00bc\u00ba\3\2\2\2")
        buf.write("\u00bc\u00bb\3\2\2\2\u00bd\21\3\2\2\2\u00be\u00bf\5\24")
        buf.write("\13\2\u00bf\u00c1\5\26\f\2\u00c0\u00c2\5\30\r\2\u00c1")
        buf.write("\u00c0\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c3\3\2\2\2")
        buf.write("\u00c3\u00c4\7\63\2\2\u00c4\23\3\2\2\2\u00c5\u00c6\7\5")
        buf.write("\2\2\u00c6\u00c7\7,\2\2\u00c7\u00c8\5<\37\2\u00c8\u00c9")
        buf.write("\7-\2\2\u00c9\u00ca\5\b\5\2\u00ca\25\3\2\2\2\u00cb\u00cc")
        buf.write("\7\6\2\2\u00cc\u00ce\5\24\13\2\u00cd\u00cb\3\2\2\2\u00ce")
        buf.write("\u00d1\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2")
        buf.write("\u00d0\27\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d2\u00d3\7\6")
        buf.write("\2\2\u00d3\u00d4\5\b\5\2\u00d4\31\3\2\2\2\u00d5\u00d9")
        buf.write("\5\34\17\2\u00d6\u00d9\5\36\20\2\u00d7\u00d9\5$\23\2\u00d8")
        buf.write("\u00d5\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d7\3\2\2\2")
        buf.write("\u00d9\33\3\2\2\2\u00da\u00db\7\7\2\2\u00db\u00dc\5<\37")
        buf.write("\2\u00dc\u00dd\5\b\5\2\u00dd\u00de\7\63\2\2\u00de\35\3")
        buf.write("\2\2\2\u00df\u00e0\7\7\2\2\u00e0\u00e1\5 \21\2\u00e1\u00e2")
        buf.write("\5<\37\2\u00e2\u00e3\7\63\2\2\u00e3\u00e4\5\"\22\2\u00e4")
        buf.write("\u00e5\5\b\5\2\u00e5\u00e6\7\63\2\2\u00e6\37\3\2\2\2\u00e7")
        buf.write("\u00e8\5\"\22\2\u00e8\u00e9\7\63\2\2\u00e9\u00f7\3\2\2")
        buf.write("\2\u00ea\u00eb\7\22\2\2\u00eb\u00f2\7@\2\2\u00ec\u00ed")
        buf.write("\7*\2\2\u00ed\u00f3\5<\37\2\u00ee\u00ef\5:\36\2\u00ef")
        buf.write("\u00f0\7*\2\2\u00f0\u00f1\5<\37\2\u00f1\u00f3\3\2\2\2")
        buf.write("\u00f2\u00ec\3\2\2\2\u00f2\u00ee\3\2\2\2\u00f3\u00f4\3")
        buf.write("\2\2\2\u00f4\u00f5\7\63\2\2\u00f5\u00f7\3\2\2\2\u00f6")
        buf.write("\u00e7\3\2\2\2\u00f6\u00ea\3\2\2\2\u00f7!\3\2\2\2\u00f8")
        buf.write("\u00f9\7@\2\2\u00f9\u00fa\5z>\2\u00fa\u00fb\5<\37\2\u00fb")
        buf.write("#\3\2\2\2\u00fc\u00fd\7\7\2\2\u00fd\u00fe\7@\2\2\u00fe")
        buf.write("\u00ff\7\62\2\2\u00ff\u0100\7@\2\2\u0100\u0101\7$\2\2")
        buf.write("\u0101\u0102\7\25\2\2\u0102\u0103\5<\37\2\u0103\u0104")
        buf.write("\5\b\5\2\u0104\u0105\7\63\2\2\u0105%\3\2\2\2\u0106\u0107")
        buf.write("\7\24\2\2\u0107\u0108\7\63\2\2\u0108\'\3\2\2\2\u0109\u010a")
        buf.write("\7\23\2\2\u010a\u010b\7\63\2\2\u010b)\3\2\2\2\u010c\u010f")
        buf.write("\5\60\31\2\u010d\u010f\5\66\34\2\u010e\u010c\3\2\2\2\u010e")
        buf.write("\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u0111\7\63\2")
        buf.write("\2\u0111+\3\2\2\2\u0112\u0114\7\b\2\2\u0113\u0115\5<\37")
        buf.write("\2\u0114\u0113\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0116")
        buf.write("\3\2\2\2\u0116\u0117\7\63\2\2\u0117-\3\2\2\2\u0118\u0119")
        buf.write("\7\t\2\2\u0119\u011a\7@\2\2\u011a\u011c\7,\2\2\u011b\u011d")
        buf.write("\5p9\2\u011c\u011b\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011e")
        buf.write("\3\2\2\2\u011e\u0120\7-\2\2\u011f\u0121\5:\36\2\u0120")
        buf.write("\u011f\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0122\3\2\2\2")
        buf.write("\u0122\u0123\5\b\5\2\u0123\u0124\7\63\2\2\u0124/\3\2\2")
        buf.write("\2\u0125\u0126\7@\2\2\u0126\u0128\7,\2\2\u0127\u0129\5")
        buf.write("\62\32\2\u0128\u0127\3\2\2\2\u0128\u0129\3\2\2\2\u0129")
        buf.write("\u012a\3\2\2\2\u012a\u012b\7-\2\2\u012b\61\3\2\2\2\u012c")
        buf.write("\u0131\5<\37\2\u012d\u012e\7\62\2\2\u012e\u0130\5<\37")
        buf.write("\2\u012f\u012d\3\2\2\2\u0130\u0133\3\2\2\2\u0131\u012f")
        buf.write("\3\2\2\2\u0131\u0132\3\2\2\2\u0132\63\3\2\2\2\u0133\u0131")
        buf.write("\3\2\2\2\u0134\u0135\7\t\2\2\u0135\u0136\7,\2\2\u0136")
        buf.write("\u0137\7@\2\2\u0137\u0138\7@\2\2\u0138\u0139\7-\2\2\u0139")
        buf.write("\u013a\7@\2\2\u013a\u013c\7,\2\2\u013b\u013d\5p9\2\u013c")
        buf.write("\u013b\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u013e\3\2\2\2")
        buf.write("\u013e\u0140\7-\2\2\u013f\u0141\5:\36\2\u0140\u013f\3")
        buf.write("\2\2\2\u0140\u0141\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0143")
        buf.write("\5\b\5\2\u0143\u0144\7\63\2\2\u0144\65\3\2\2\2\u0145\u0146")
        buf.write("\5j\66\2\u0146\u0147\7+\2\2\u0147\u0148\5\60\31\2\u0148")
        buf.write("\67\3\2\2\2\u0149\u014a\t\2\2\2\u014a9\3\2\2\2\u014b\u014f")
        buf.write("\58\35\2\u014c\u014f\7@\2\2\u014d\u014f\5N(\2\u014e\u014b")
        buf.write("\3\2\2\2\u014e\u014c\3\2\2\2\u014e\u014d\3\2\2\2\u014f")
        buf.write(";\3\2\2\2\u0150\u0151\b\37\1\2\u0151\u0152\5> \2\u0152")
        buf.write("\u0158\3\2\2\2\u0153\u0154\f\4\2\2\u0154\u0155\7\"\2\2")
        buf.write("\u0155\u0157\5> \2\u0156\u0153\3\2\2\2\u0157\u015a\3\2")
        buf.write("\2\2\u0158\u0156\3\2\2\2\u0158\u0159\3\2\2\2\u0159=\3")
        buf.write("\2\2\2\u015a\u0158\3\2\2\2\u015b\u015c\b \1\2\u015c\u015d")
        buf.write("\5@!\2\u015d\u0163\3\2\2\2\u015e\u015f\f\4\2\2\u015f\u0160")
        buf.write("\7!\2\2\u0160\u0162\5@!\2\u0161\u015e\3\2\2\2\u0162\u0165")
        buf.write("\3\2\2\2\u0163\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164")
        buf.write("?\3\2\2\2\u0165\u0163\3\2\2\2\u0166\u0167\b!\1\2\u0167")
        buf.write("\u0168\5B\"\2\u0168\u016f\3\2\2\2\u0169\u016a\f\4\2\2")
        buf.write("\u016a\u016b\5x=\2\u016b\u016c\5B\"\2\u016c\u016e\3\2")
        buf.write("\2\2\u016d\u0169\3\2\2\2\u016e\u0171\3\2\2\2\u016f\u016d")
        buf.write("\3\2\2\2\u016f\u0170\3\2\2\2\u0170A\3\2\2\2\u0171\u016f")
        buf.write("\3\2\2\2\u0172\u0173\b\"\1\2\u0173\u0174\5D#\2\u0174\u017b")
        buf.write("\3\2\2\2\u0175\u0176\f\4\2\2\u0176\u0177\5v<\2\u0177\u0178")
        buf.write("\5D#\2\u0178\u017a\3\2\2\2\u0179\u0175\3\2\2\2\u017a\u017d")
        buf.write("\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c")
        buf.write("C\3\2\2\2\u017d\u017b\3\2\2\2\u017e\u017f\b#\1\2\u017f")
        buf.write("\u0180\5F$\2\u0180\u0187\3\2\2\2\u0181\u0182\f\4\2\2\u0182")
        buf.write("\u0183\5t;\2\u0183\u0184\5F$\2\u0184\u0186\3\2\2\2\u0185")
        buf.write("\u0181\3\2\2\2\u0186\u0189\3\2\2\2\u0187\u0185\3\2\2\2")
        buf.write("\u0187\u0188\3\2\2\2\u0188E\3\2\2\2\u0189\u0187\3\2\2")
        buf.write("\2\u018a\u018b\t\3\2\2\u018b\u018e\5F$\2\u018c\u018e\5")
        buf.write("H%\2\u018d\u018a\3\2\2\2\u018d\u018c\3\2\2\2\u018eG\3")
        buf.write("\2\2\2\u018f\u0194\5h\65\2\u0190\u0194\5\\/\2\u0191\u0194")
        buf.write("\5\66\34\2\u0192\u0194\5L\'\2\u0193\u018f\3\2\2\2\u0193")
        buf.write("\u0190\3\2\2\2\u0193\u0191\3\2\2\2\u0193\u0192\3\2\2\2")
        buf.write("\u0194I\3\2\2\2\u0195\u0196\7,\2\2\u0196\u0197\5<\37\2")
        buf.write("\u0197\u0198\7-\2\2\u0198K\3\2\2\2\u0199\u01a4\7\65\2")
        buf.write("\2\u019a\u01a4\7:\2\2\u019b\u01a4\7;\2\2\u019c\u01a4\7")
        buf.write("<\2\2\u019d\u01a4\7=\2\2\u019e\u01a4\5T+\2\u019f\u01a4")
        buf.write("\5b\62\2\u01a0\u01a4\7@\2\2\u01a1\u01a4\5\60\31\2\u01a2")
        buf.write("\u01a4\5J&\2\u01a3\u0199\3\2\2\2\u01a3\u019a\3\2\2\2\u01a3")
        buf.write("\u019b\3\2\2\2\u01a3\u019c\3\2\2\2\u01a3\u019d\3\2\2\2")
        buf.write("\u01a3\u019e\3\2\2\2\u01a3\u019f\3\2\2\2\u01a3\u01a0\3")
        buf.write("\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a2\3\2\2\2\u01a4M")
        buf.write("\3\2\2\2\u01a5\u01a6\5P)\2\u01a6\u01a7\5N(\2\u01a7\u01ae")
        buf.write("\3\2\2\2\u01a8\u01ab\5P)\2\u01a9\u01ac\58\35\2\u01aa\u01ac")
        buf.write("\7@\2\2\u01ab\u01a9\3\2\2\2\u01ab\u01aa\3\2\2\2\u01ac")
        buf.write("\u01ae\3\2\2\2\u01ad\u01a5\3\2\2\2\u01ad\u01a8\3\2\2\2")
        buf.write("\u01aeO\3\2\2\2\u01af\u01b0\7.\2\2\u01b0\u01b1\t\4\2\2")
        buf.write("\u01b1\u01b2\7/\2\2\u01b2Q\3\2\2\2\u01b3\u01b4\7.\2\2")
        buf.write("\u01b4\u01b5\5<\37\2\u01b5\u01b6\7/\2\2\u01b6S\3\2\2\2")
        buf.write("\u01b7\u01b8\5N(\2\u01b8\u01b9\7\60\2\2\u01b9\u01ba\5")
        buf.write("V,\2\u01ba\u01bb\7\61\2\2\u01bbU\3\2\2\2\u01bc\u01c1\5")
        buf.write("X-\2\u01bd\u01be\7\62\2\2\u01be\u01c0\5X-\2\u01bf\u01bd")
        buf.write("\3\2\2\2\u01c0\u01c3\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c1")
        buf.write("\u01c2\3\2\2\2\u01c2W\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c4")
        buf.write("\u01cd\7\65\2\2\u01c5\u01cd\7:\2\2\u01c6\u01cd\7<\2\2")
        buf.write("\u01c7\u01cd\7;\2\2\u01c8\u01cd\7=\2\2\u01c9\u01cd\7@")
        buf.write("\2\2\u01ca\u01cd\5b\62\2\u01cb\u01cd\5Z.\2\u01cc\u01c4")
        buf.write("\3\2\2\2\u01cc\u01c5\3\2\2\2\u01cc\u01c6\3\2\2\2\u01cc")
        buf.write("\u01c7\3\2\2\2\u01cc\u01c8\3\2\2\2\u01cc\u01c9\3\2\2\2")
        buf.write("\u01cc\u01ca\3\2\2\2\u01cc\u01cb\3\2\2\2\u01cdY\3\2\2")
        buf.write("\2\u01ce\u01cf\7\60\2\2\u01cf\u01d0\5V,\2\u01d0\u01d1")
        buf.write("\7\61\2\2\u01d1[\3\2\2\2\u01d2\u01d7\5j\66\2\u01d3\u01d4")
        buf.write("\7+\2\2\u01d4\u01d8\7@\2\2\u01d5\u01d6\7+\2\2\u01d6\u01d8")
        buf.write("\5\60\31\2\u01d7\u01d3\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d8")
        buf.write("\u01da\3\2\2\2\u01d9\u01db\5R*\2\u01da\u01d9\3\2\2\2\u01db")
        buf.write("\u01dc\3\2\2\2\u01dc\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2")
        buf.write("\u01dd\u01e5\3\2\2\2\u01de\u01e0\5L\'\2\u01df\u01e1\5")
        buf.write("R*\2\u01e0\u01df\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e0")
        buf.write("\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3\u01e5\3\2\2\2\u01e4")
        buf.write("\u01d2\3\2\2\2\u01e4\u01de\3\2\2\2\u01e5]\3\2\2\2\u01e6")
        buf.write("\u01e7\7\n\2\2\u01e7\u01e8\7@\2\2\u01e8\u01e9\7\13\2\2")
        buf.write("\u01e9\u01eb\7\60\2\2\u01ea\u01ec\5`\61\2\u01eb\u01ea")
        buf.write("\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed")
        buf.write("\u01ee\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef\u01f0\7\61\2")
        buf.write("\2\u01f0\u01f1\7\63\2\2\u01f1_\3\2\2\2\u01f2\u01f3\7@")
        buf.write("\2\2\u01f3\u01f4\5:\36\2\u01f4\u01f5\7\63\2\2\u01f5a\3")
        buf.write("\2\2\2\u01f6\u01f7\7@\2\2\u01f7\u01f9\7\60\2\2\u01f8\u01fa")
        buf.write("\5d\63\2\u01f9\u01f8\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa")
        buf.write("\u01fb\3\2\2\2\u01fb\u01fc\7\61\2\2\u01fcc\3\2\2\2\u01fd")
        buf.write("\u0202\5f\64\2\u01fe\u01ff\7\62\2\2\u01ff\u0201\5f\64")
        buf.write("\2\u0200\u01fe\3\2\2\2\u0201\u0204\3\2\2\2\u0202\u0200")
        buf.write("\3\2\2\2\u0202\u0203\3\2\2\2\u0203e\3\2\2\2\u0204\u0202")
        buf.write("\3\2\2\2\u0205\u0206\7@\2\2\u0206\u0207\7\64\2\2\u0207")
        buf.write("\u0208\5<\37\2\u0208g\3\2\2\2\u0209\u020a\5j\66\2\u020a")
        buf.write("\u020b\7+\2\2\u020b\u020c\7@\2\2\u020ci\3\2\2\2\u020d")
        buf.write("\u0219\5L\'\2\u020e\u020f\7+\2\2\u020f\u0218\7@\2\2\u0210")
        buf.write("\u0212\5R*\2\u0211\u0210\3\2\2\2\u0212\u0213\3\2\2\2\u0213")
        buf.write("\u0211\3\2\2\2\u0213\u0214\3\2\2\2\u0214\u0218\3\2\2\2")
        buf.write("\u0215\u0216\7+\2\2\u0216\u0218\5\60\31\2\u0217\u020e")
        buf.write("\3\2\2\2\u0217\u0211\3\2\2\2\u0217\u0215\3\2\2\2\u0218")
        buf.write("\u021b\3\2\2\2\u0219\u0217\3\2\2\2\u0219\u021a\3\2\2\2")
        buf.write("\u021ak\3\2\2\2\u021b\u0219\3\2\2\2\u021c\u021d\7\n\2")
        buf.write("\2\u021d\u021e\7@\2\2\u021e\u021f\7\f\2\2\u021f\u0221")
        buf.write("\7\60\2\2\u0220\u0222\5n8\2\u0221\u0220\3\2\2\2\u0222")
        buf.write("\u0223\3\2\2\2\u0223\u0221\3\2\2\2\u0223\u0224\3\2\2\2")
        buf.write("\u0224\u0225\3\2\2\2\u0225\u0226\7\61\2\2\u0226\u0227")
        buf.write("\7\63\2\2\u0227m\3\2\2\2\u0228\u0229\7@\2\2\u0229\u022b")
        buf.write("\7,\2\2\u022a\u022c\5p9\2\u022b\u022a\3\2\2\2\u022b\u022c")
        buf.write("\3\2\2\2\u022c\u022d\3\2\2\2\u022d\u022f\7-\2\2\u022e")
        buf.write("\u0230\5:\36\2\u022f\u022e\3\2\2\2\u022f\u0230\3\2\2\2")
        buf.write("\u0230\u0231\3\2\2\2\u0231\u0232\7\63\2\2\u0232o\3\2\2")
        buf.write("\2\u0233\u0238\5r:\2\u0234\u0235\7\62\2\2\u0235\u0237")
        buf.write("\5r:\2\u0236\u0234\3\2\2\2\u0237\u023a\3\2\2\2\u0238\u0236")
        buf.write("\3\2\2\2\u0238\u0239\3\2\2\2\u0239q\3\2\2\2\u023a\u0238")
        buf.write("\3\2\2\2\u023b\u0240\7@\2\2\u023c\u023d\7\62\2\2\u023d")
        buf.write("\u023f\7@\2\2\u023e\u023c\3\2\2\2\u023f\u0242\3\2\2\2")
        buf.write("\u0240\u023e\3\2\2\2\u0240\u0241\3\2\2\2\u0241\u0243\3")
        buf.write("\2\2\2\u0242\u0240\3\2\2\2\u0243\u0244\5:\36\2\u0244s")
        buf.write("\3\2\2\2\u0245\u0246\t\5\2\2\u0246u\3\2\2\2\u0247\u0248")
        buf.write("\t\6\2\2\u0248w\3\2\2\2\u0249\u024a\t\7\2\2\u024ay\3\2")
        buf.write("\2\2\u024b\u024c\t\b\2\2\u024c{\3\2\2\2\u024d\u024e\t")
        buf.write("\t\2\2\u024e}\3\2\2\2\61\u0081\u008b\u0097\u009d\u00aa")
        buf.write("\u00bc\u00c1\u00cf\u00d8\u00f2\u00f6\u010e\u0114\u011c")
        buf.write("\u0120\u0128\u0131\u013c\u0140\u014e\u0158\u0163\u016f")
        buf.write("\u017b\u0187\u018d\u0193\u01a3\u01ab\u01ad\u01c1\u01cc")
        buf.write("\u01d7\u01dc\u01e2\u01e4\u01ed\u01f9\u0202\u0213\u0217")
        buf.write("\u0219\u0223\u022b\u022f\u0238\u0240")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'if'", "'else'", 
                     "'for'", "'return'", "'func'", "'type'", "'struct'", 
                     "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
                     "'const'", "'var'", "'continue'", "'break'", "'range'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", 
                     "'>='", "'<='", "'>'", "'<'", "'&&'", "'||'", "'!'", 
                     "':='", "'+='", "'-='", "'*='", "'/='", "'%='", "'='", 
                     "'.'", "'('", "')'", "'['", "']'", "'{'", "'}'", "','", 
                     "';'", "':'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'nil'" ]

    symbolicNames = [ "<INVALID>", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", 
                      "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                      "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                      "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "ADD", 
                      "SUB", "MULTIPLY", "DIVIDE", "REMAIN", "COMPARE_STR", 
                      "NOT_EQ", "GREATER_OR_EQ", "LESS_OR_EQ", "GREATER", 
                      "LESS", "AND", "OR", "NOT", "ASSIGNMENT_SIGN", "SHORT_ADD", 
                      "SHORT_SUB", "SHORT_MULTIPLY", "SHORT_DIVIDE", "SHORT_REMAIN", 
                      "EQUAL", "DOT", "OPEN_PARENTHESIS", "CLOSE_PARENTHESIS", 
                      "OPEN_BRACKET", "CLOSE_BRACKET", "OPEN_BRACE", "CLOSE_BRACE", 
                      "COMMA", "SEMICOLON", "COLON", "INTEGER_LITERAL", 
                      "DECIMAL_INT", "BINARY_INT", "OCTAL_INT", "HEXA_INT", 
                      "FLOAT_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
                      "NIL_LITERAL", "NEWLINE", "WHITESPACE", "IDENTIFIER", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_stmt = 2
    RULE_block = 3
    RULE_var_decl = 4
    RULE_const_decl = 5
    RULE_assign_stmt = 6
    RULE_lhs = 7
    RULE_if_stmt = 8
    RULE_only_if_stmt = 9
    RULE_else_if_list = 10
    RULE_else_stmt = 11
    RULE_for_stmt = 12
    RULE_basic_for_loop = 13
    RULE_for_loop_initial = 14
    RULE_initialization = 15
    RULE_update = 16
    RULE_for_loop_range = 17
    RULE_break_stmt = 18
    RULE_continue_stmt = 19
    RULE_call_stmt = 20
    RULE_return_stmt = 21
    RULE_func_decl = 22
    RULE_func_call = 23
    RULE_argument_list = 24
    RULE_method_decl = 25
    RULE_method_call = 26
    RULE_primitive_type = 27
    RULE_typ = 28
    RULE_expr = 29
    RULE_expr1 = 30
    RULE_expr2 = 31
    RULE_expr3 = 32
    RULE_expr4 = 33
    RULE_expr5 = 34
    RULE_expr6 = 35
    RULE_sub_expr = 36
    RULE_operand = 37
    RULE_array_type = 38
    RULE_array_literal_box = 39
    RULE_array_access_box = 40
    RULE_array_literal = 41
    RULE_array_ele_list = 42
    RULE_array_ele = 43
    RULE_short_array_literal = 44
    RULE_array_access = 45
    RULE_struct_decl = 46
    RULE_struct_field = 47
    RULE_struct_literal = 48
    RULE_struct_ele_list = 49
    RULE_struct_ele = 50
    RULE_struct_access = 51
    RULE_struct_array_method = 52
    RULE_interface_decl = 53
    RULE_interface_method = 54
    RULE_param_list = 55
    RULE_param_decl = 56
    RULE_arith_high_operator = 57
    RULE_arith_low_operator = 58
    RULE_relational_operator = 59
    RULE_assign_operator = 60
    RULE_comment = 61

    ruleNames =  [ "program", "decl", "stmt", "block", "var_decl", "const_decl", 
                   "assign_stmt", "lhs", "if_stmt", "only_if_stmt", "else_if_list", 
                   "else_stmt", "for_stmt", "basic_for_loop", "for_loop_initial", 
                   "initialization", "update", "for_loop_range", "break_stmt", 
                   "continue_stmt", "call_stmt", "return_stmt", "func_decl", 
                   "func_call", "argument_list", "method_decl", "method_call", 
                   "primitive_type", "typ", "expr", "expr1", "expr2", "expr3", 
                   "expr4", "expr5", "expr6", "sub_expr", "operand", "array_type", 
                   "array_literal_box", "array_access_box", "array_literal", 
                   "array_ele_list", "array_ele", "short_array_literal", 
                   "array_access", "struct_decl", "struct_field", "struct_literal", 
                   "struct_ele_list", "struct_ele", "struct_access", "struct_array_method", 
                   "interface_decl", "interface_method", "param_list", "param_decl", 
                   "arith_high_operator", "arith_low_operator", "relational_operator", 
                   "assign_operator", "comment" ]

    EOF = Token.EOF
    SINGLE_LINE_COMMENT=1
    MULTI_LINE_COMMENT=2
    IF=3
    ELSE=4
    FOR=5
    RETURN=6
    FUNC=7
    TYPE=8
    STRUCT=9
    INTERFACE=10
    STRING=11
    INT=12
    FLOAT=13
    BOOLEAN=14
    CONST=15
    VAR=16
    CONTINUE=17
    BREAK=18
    RANGE=19
    ADD=20
    SUB=21
    MULTIPLY=22
    DIVIDE=23
    REMAIN=24
    COMPARE_STR=25
    NOT_EQ=26
    GREATER_OR_EQ=27
    LESS_OR_EQ=28
    GREATER=29
    LESS=30
    AND=31
    OR=32
    NOT=33
    ASSIGNMENT_SIGN=34
    SHORT_ADD=35
    SHORT_SUB=36
    SHORT_MULTIPLY=37
    SHORT_DIVIDE=38
    SHORT_REMAIN=39
    EQUAL=40
    DOT=41
    OPEN_PARENTHESIS=42
    CLOSE_PARENTHESIS=43
    OPEN_BRACKET=44
    CLOSE_BRACKET=45
    OPEN_BRACE=46
    CLOSE_BRACE=47
    COMMA=48
    SEMICOLON=49
    COLON=50
    INTEGER_LITERAL=51
    DECIMAL_INT=52
    BINARY_INT=53
    OCTAL_INT=54
    HEXA_INT=55
    FLOAT_LITERAL=56
    STRING_LITERAL=57
    BOOLEAN_LITERAL=58
    NIL_LITERAL=59
    NEWLINE=60
    WHITESPACE=61
    IDENTIFIER=62
    ILLEGAL_ESCAPE=63
    UNCLOSE_STRING=64
    ERROR_CHAR=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 124
                self.decl()
                self.state = 127 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR))) != 0)):
                    break

            self.state = 129
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def struct_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declContext,0)


        def interface_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.const_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 133
                self.struct_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 134
                self.interface_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 135
                self.func_decl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 136
                self.method_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Return_stmtContext,0)


        def comment(self):
            return self.getTypedRuleContext(MiniGoParser.CommentContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.const_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                self.assign_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 142
                self.if_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 143
                self.for_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 144
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 145
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 146
                self.call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 147
                self.return_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 148
                self.comment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(MiniGoParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(MiniGoParser.CLOSE_BRACE, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(MiniGoParser.OPEN_BRACE)
            self.state = 153 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 152
                self.stmt()
                self.state = 155 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.SINGLE_LINE_COMMENT) | (1 << MiniGoParser.MULTI_LINE_COMMENT) | (1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.OPEN_PARENTHESIS) | (1 << MiniGoParser.OPEN_BRACKET) | (1 << MiniGoParser.INTEGER_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
                    break

            self.state = 157
            self.match(MiniGoParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = MiniGoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(MiniGoParser.VAR)
            self.state = 160
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 161
                self.typ()
                pass

            elif la_ == 2:
                self.state = 162
                self.match(MiniGoParser.EQUAL)
                self.state = 163
                self.expr(0)
                pass

            elif la_ == 3:
                self.state = 164
                self.typ()
                self.state = 165
                self.match(MiniGoParser.EQUAL)
                self.state = 166
                self.expr(0)
                pass


            self.state = 170
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl" ):
                return visitor.visitConst_decl(self)
            else:
                return visitor.visitChildren(self)




    def const_decl(self):

        localctx = MiniGoParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(MiniGoParser.CONST)
            self.state = 173
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 174
            self.match(MiniGoParser.EQUAL)
            self.state = 175
            self.expr(0)
            self.state = 176
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def assign_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_operatorContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = MiniGoParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.lhs()
            self.state = 179
            self.assign_operator()
            self.state = 180
            self.expr(0)
            self.state = 181
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def struct_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_accessContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_lhs)
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.struct_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
                self.array_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def only_if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Only_if_stmtContext,0)


        def else_if_list(self):
            return self.getTypedRuleContext(MiniGoParser.Else_if_listContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def else_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Else_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = MiniGoParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.only_if_stmt()
            self.state = 189
            self.else_if_list()
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 190
                self.else_stmt()


            self.state = 193
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Only_if_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def OPEN_PARENTHESIS(self):
            return self.getToken(MiniGoParser.OPEN_PARENTHESIS, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def CLOSE_PARENTHESIS(self):
            return self.getToken(MiniGoParser.CLOSE_PARENTHESIS, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_only_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOnly_if_stmt" ):
                return visitor.visitOnly_if_stmt(self)
            else:
                return visitor.visitChildren(self)




    def only_if_stmt(self):

        localctx = MiniGoParser.Only_if_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_only_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(MiniGoParser.IF)
            self.state = 196
            self.match(MiniGoParser.OPEN_PARENTHESIS)
            self.state = 197
            self.expr(0)
            self.state = 198
            self.match(MiniGoParser.CLOSE_PARENTHESIS)
            self.state = 199
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ELSE)
            else:
                return self.getToken(MiniGoParser.ELSE, i)

        def only_if_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Only_if_stmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Only_if_stmtContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_if_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if_list" ):
                return visitor.visitElse_if_list(self)
            else:
                return visitor.visitChildren(self)




    def else_if_list(self):

        localctx = MiniGoParser.Else_if_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_else_if_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 201
                    self.match(MiniGoParser.ELSE)
                    self.state = 202
                    self.only_if_stmt() 
                self.state = 207
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = MiniGoParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(MiniGoParser.ELSE)
            self.state = 209
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_for_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Basic_for_loopContext,0)


        def for_loop_initial(self):
            return self.getTypedRuleContext(MiniGoParser.For_loop_initialContext,0)


        def for_loop_range(self):
            return self.getTypedRuleContext(MiniGoParser.For_loop_rangeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = MiniGoParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_for_stmt)
        try:
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.basic_for_loop()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.for_loop_initial()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 213
                self.for_loop_range()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_for_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_basic_for_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_for_loop" ):
                return visitor.visitBasic_for_loop(self)
            else:
                return visitor.visitChildren(self)




    def basic_for_loop(self):

        localctx = MiniGoParser.Basic_for_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_basic_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(MiniGoParser.FOR)
            self.state = 217
            self.expr(0)
            self.state = 218
            self.block()
            self.state = 219
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loop_initialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def initialization(self):
            return self.getTypedRuleContext(MiniGoParser.InitializationContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def update(self):
            return self.getTypedRuleContext(MiniGoParser.UpdateContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_loop_initial

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop_initial" ):
                return visitor.visitFor_loop_initial(self)
            else:
                return visitor.visitChildren(self)




    def for_loop_initial(self):

        localctx = MiniGoParser.For_loop_initialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_for_loop_initial)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(MiniGoParser.FOR)
            self.state = 222
            self.initialization()
            self.state = 223
            self.expr(0)
            self.state = 224
            self.match(MiniGoParser.SEMICOLON)
            self.state = 225
            self.update()
            self.state = 226
            self.block()
            self.state = 227
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def update(self):
            return self.getTypedRuleContext(MiniGoParser.UpdateContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_initialization

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitialization" ):
                return visitor.visitInitialization(self)
            else:
                return visitor.visitChildren(self)




    def initialization(self):

        localctx = MiniGoParser.InitializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_initialization)
        try:
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.update()
                self.state = 230
                self.match(MiniGoParser.SEMICOLON)
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.match(MiniGoParser.VAR)
                self.state = 233
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 240
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.EQUAL]:
                    self.state = 234
                    self.match(MiniGoParser.EQUAL)
                    self.state = 235
                    self.expr(0)
                    pass
                elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.OPEN_BRACKET, MiniGoParser.IDENTIFIER]:
                    self.state = 236
                    self.typ()
                    self.state = 237
                    self.match(MiniGoParser.EQUAL)
                    self.state = 238
                    self.expr(0)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 242
                self.match(MiniGoParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def assign_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_operatorContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_update

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate" ):
                return visitor.visitUpdate(self)
            else:
                return visitor.visitChildren(self)




    def update(self):

        localctx = MiniGoParser.UpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 247
            self.assign_operator()
            self.state = 248
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loop_rangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ASSIGNMENT_SIGN(self):
            return self.getToken(MiniGoParser.ASSIGNMENT_SIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_for_loop_range

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop_range" ):
                return visitor.visitFor_loop_range(self)
            else:
                return visitor.visitChildren(self)




    def for_loop_range(self):

        localctx = MiniGoParser.For_loop_rangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_for_loop_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(MiniGoParser.FOR)
            self.state = 251
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 252
            self.match(MiniGoParser.COMMA)
            self.state = 253
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 254
            self.match(MiniGoParser.ASSIGNMENT_SIGN)
            self.state = 255
            self.match(MiniGoParser.RANGE)
            self.state = 256
            self.expr(0)
            self.state = 257
            self.block()
            self.state = 258
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = MiniGoParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(MiniGoParser.BREAK)
            self.state = 261
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = MiniGoParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(MiniGoParser.CONTINUE)
            self.state = 264
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def method_call(self):
            return self.getTypedRuleContext(MiniGoParser.Method_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = MiniGoParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 266
                self.func_call()
                pass

            elif la_ == 2:
                self.state = 267
                self.method_call()
                pass


            self.state = 270
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = MiniGoParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(MiniGoParser.RETURN)
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.OPEN_PARENTHESIS) | (1 << MiniGoParser.OPEN_BRACKET) | (1 << MiniGoParser.INTEGER_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 273
                self.expr(0)


            self.state = 276
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def OPEN_PARENTHESIS(self):
            return self.getToken(MiniGoParser.OPEN_PARENTHESIS, 0)

        def CLOSE_PARENTHESIS(self):
            return self.getToken(MiniGoParser.CLOSE_PARENTHESIS, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def param_list(self):
            return self.getTypedRuleContext(MiniGoParser.Param_listContext,0)


        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = MiniGoParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(MiniGoParser.FUNC)
            self.state = 279
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 280
            self.match(MiniGoParser.OPEN_PARENTHESIS)
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 281
                self.param_list()


            self.state = 284
            self.match(MiniGoParser.CLOSE_PARENTHESIS)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.OPEN_BRACKET) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 285
                self.typ()


            self.state = 288
            self.block()
            self.state = 289
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def OPEN_PARENTHESIS(self):
            return self.getToken(MiniGoParser.OPEN_PARENTHESIS, 0)

        def CLOSE_PARENTHESIS(self):
            return self.getToken(MiniGoParser.CLOSE_PARENTHESIS, 0)

        def argument_list(self):
            return self.getTypedRuleContext(MiniGoParser.Argument_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 292
            self.match(MiniGoParser.OPEN_PARENTHESIS)
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.OPEN_PARENTHESIS) | (1 << MiniGoParser.OPEN_BRACKET) | (1 << MiniGoParser.INTEGER_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 293
                self.argument_list()


            self.state = 296
            self.match(MiniGoParser.CLOSE_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_argument_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument_list" ):
                return visitor.visitArgument_list(self)
            else:
                return visitor.visitChildren(self)




    def argument_list(self):

        localctx = MiniGoParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.expr(0)
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 299
                self.match(MiniGoParser.COMMA)
                self.state = 300
                self.expr(0)
                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def OPEN_PARENTHESIS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.OPEN_PARENTHESIS)
            else:
                return self.getToken(MiniGoParser.OPEN_PARENTHESIS, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def CLOSE_PARENTHESIS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.CLOSE_PARENTHESIS)
            else:
                return self.getToken(MiniGoParser.CLOSE_PARENTHESIS, i)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def param_list(self):
            return self.getTypedRuleContext(MiniGoParser.Param_listContext,0)


        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = MiniGoParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(MiniGoParser.FUNC)
            self.state = 307
            self.match(MiniGoParser.OPEN_PARENTHESIS)
            self.state = 308
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 309
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 310
            self.match(MiniGoParser.CLOSE_PARENTHESIS)
            self.state = 311
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 312
            self.match(MiniGoParser.OPEN_PARENTHESIS)
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 313
                self.param_list()


            self.state = 316
            self.match(MiniGoParser.CLOSE_PARENTHESIS)
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.OPEN_BRACKET) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 317
                self.typ()


            self.state = 320
            self.block()
            self.state = 321
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_array_method(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_array_methodContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_call" ):
                return visitor.visitMethod_call(self)
            else:
                return visitor.visitChildren(self)




    def method_call(self):

        localctx = MiniGoParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_method_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.struct_array_method()
            self.state = 324
            self.match(MiniGoParser.DOT)
            self.state = 325
            self.func_call()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = MiniGoParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = MiniGoParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_typ)
        try:
            self.state = 332
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.primitive_type()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [MiniGoParser.OPEN_BRACKET]:
                self.enterOuterAlt(localctx, 3)
                self.state = 331
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 342
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 337
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 338
                    self.match(MiniGoParser.OR)
                    self.state = 339
                    self.expr1(0) 
                self.state = 344
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 353
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 348
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 349
                    self.match(MiniGoParser.AND)
                    self.state = 350
                    self.expr2(0) 
                self.state = 355
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def relational_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Relational_operatorContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 365
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 359
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 360
                    self.relational_operator()
                    self.state = 361
                    self.expr3(0) 
                self.state = 367
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def arith_low_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Arith_low_operatorContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 377
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 371
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 372
                    self.arith_low_operator()
                    self.state = 373
                    self.expr4(0) 
                self.state = 379
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def arith_high_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Arith_high_operatorContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 389
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 383
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 384
                    self.arith_high_operator()
                    self.state = 385
                    self.expr5() 
                self.state = 391
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 395
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 393
                self.expr5()
                pass
            elif token in [MiniGoParser.OPEN_PARENTHESIS, MiniGoParser.OPEN_BRACKET, MiniGoParser.INTEGER_LITERAL, MiniGoParser.FLOAT_LITERAL, MiniGoParser.STRING_LITERAL, MiniGoParser.BOOLEAN_LITERAL, MiniGoParser.NIL_LITERAL, MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_accessContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def method_call(self):
            return self.getTypedRuleContext(MiniGoParser.Method_callContext,0)


        def operand(self):
            return self.getTypedRuleContext(MiniGoParser.OperandContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = MiniGoParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expr6)
        try:
            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.struct_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
                self.array_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 399
                self.method_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 400
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sub_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PARENTHESIS(self):
            return self.getToken(MiniGoParser.OPEN_PARENTHESIS, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def CLOSE_PARENTHESIS(self):
            return self.getToken(MiniGoParser.CLOSE_PARENTHESIS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_sub_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub_expr" ):
                return visitor.visitSub_expr(self)
            else:
                return visitor.visitChildren(self)




    def sub_expr(self):

        localctx = MiniGoParser.Sub_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_sub_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(MiniGoParser.OPEN_PARENTHESIS)
            self.state = 404
            self.expr(0)
            self.state = 405
            self.match(MiniGoParser.CLOSE_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(MiniGoParser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(MiniGoParser.FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(MiniGoParser.STRING_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(MiniGoParser.BOOLEAN_LITERAL, 0)

        def NIL_LITERAL(self):
            return self.getToken(MiniGoParser.NIL_LITERAL, 0)

        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def sub_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Sub_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MiniGoParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_operand)
        try:
            self.state = 417
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.match(MiniGoParser.INTEGER_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.match(MiniGoParser.FLOAT_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 409
                self.match(MiniGoParser.STRING_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 410
                self.match(MiniGoParser.BOOLEAN_LITERAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 411
                self.match(MiniGoParser.NIL_LITERAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 412
                self.array_literal()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 413
                self.struct_literal()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 414
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 415
                self.func_call()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 416
                self.sub_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_literal_box(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literal_boxContext,0)


        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = MiniGoParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_array_type)
        try:
            self.state = 427
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 419
                self.array_literal_box()
                self.state = 420
                self.array_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 422
                self.array_literal_box()
                self.state = 425
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                    self.state = 423
                    self.primitive_type()
                    pass
                elif token in [MiniGoParser.IDENTIFIER]:
                    self.state = 424
                    self.match(MiniGoParser.IDENTIFIER)
                    pass
                else:
                    raise NoViableAltException(self)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literal_boxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(MiniGoParser.OPEN_BRACKET, 0)

        def CLOSE_BRACKET(self):
            return self.getToken(MiniGoParser.CLOSE_BRACKET, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(MiniGoParser.INTEGER_LITERAL, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal_box

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal_box" ):
                return visitor.visitArray_literal_box(self)
            else:
                return visitor.visitChildren(self)




    def array_literal_box(self):

        localctx = MiniGoParser.Array_literal_boxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_array_literal_box)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(MiniGoParser.OPEN_BRACKET)
            self.state = 430
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.INTEGER_LITERAL or _la==MiniGoParser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 431
            self.match(MiniGoParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_access_boxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(MiniGoParser.OPEN_BRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(MiniGoParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_access_box

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_access_box" ):
                return visitor.visitArray_access_box(self)
            else:
                return visitor.visitChildren(self)




    def array_access_box(self):

        localctx = MiniGoParser.Array_access_boxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_array_access_box)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.match(MiniGoParser.OPEN_BRACKET)
            self.state = 434
            self.expr(0)
            self.state = 435
            self.match(MiniGoParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def OPEN_BRACE(self):
            return self.getToken(MiniGoParser.OPEN_BRACE, 0)

        def array_ele_list(self):
            return self.getTypedRuleContext(MiniGoParser.Array_ele_listContext,0)


        def CLOSE_BRACE(self):
            return self.getToken(MiniGoParser.CLOSE_BRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = MiniGoParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.array_type()
            self.state = 438
            self.match(MiniGoParser.OPEN_BRACE)
            self.state = 439
            self.array_ele_list()
            self.state = 440
            self.match(MiniGoParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_ele_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_ele(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_eleContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_eleContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_ele_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_ele_list" ):
                return visitor.visitArray_ele_list(self)
            else:
                return visitor.visitChildren(self)




    def array_ele_list(self):

        localctx = MiniGoParser.Array_ele_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_array_ele_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.array_ele()
            self.state = 447
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 443
                self.match(MiniGoParser.COMMA)
                self.state = 444
                self.array_ele()
                self.state = 449
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_eleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(MiniGoParser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(MiniGoParser.FLOAT_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(MiniGoParser.BOOLEAN_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(MiniGoParser.STRING_LITERAL, 0)

        def NIL_LITERAL(self):
            return self.getToken(MiniGoParser.NIL_LITERAL, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def short_array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Short_array_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_ele

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_ele" ):
                return visitor.visitArray_ele(self)
            else:
                return visitor.visitChildren(self)




    def array_ele(self):

        localctx = MiniGoParser.Array_eleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_array_ele)
        try:
            self.state = 458
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 450
                self.match(MiniGoParser.INTEGER_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 451
                self.match(MiniGoParser.FLOAT_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 452
                self.match(MiniGoParser.BOOLEAN_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 453
                self.match(MiniGoParser.STRING_LITERAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 454
                self.match(MiniGoParser.NIL_LITERAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 455
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 456
                self.struct_literal()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 457
                self.short_array_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Short_array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(MiniGoParser.OPEN_BRACE, 0)

        def array_ele_list(self):
            return self.getTypedRuleContext(MiniGoParser.Array_ele_listContext,0)


        def CLOSE_BRACE(self):
            return self.getToken(MiniGoParser.CLOSE_BRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_short_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShort_array_literal" ):
                return visitor.visitShort_array_literal(self)
            else:
                return visitor.visitChildren(self)




    def short_array_literal(self):

        localctx = MiniGoParser.Short_array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_short_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.match(MiniGoParser.OPEN_BRACE)
            self.state = 461
            self.array_ele_list()
            self.state = 462
            self.match(MiniGoParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_array_method(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_array_methodContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def array_access_box(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_access_boxContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_access_boxContext,i)


        def operand(self):
            return self.getTypedRuleContext(MiniGoParser.OperandContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_access" ):
                return visitor.visitArray_access(self)
            else:
                return visitor.visitChildren(self)




    def array_access(self):

        localctx = MiniGoParser.Array_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_array_access)
        try:
            self.state = 482
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 464
                self.struct_array_method()
                self.state = 469
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                if la_ == 1:
                    self.state = 465
                    self.match(MiniGoParser.DOT)
                    self.state = 466
                    self.match(MiniGoParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 467
                    self.match(MiniGoParser.DOT)
                    self.state = 468
                    self.func_call()
                    pass


                self.state = 472 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 471
                        self.array_access_box()

                    else:
                        raise NoViableAltException(self)
                    self.state = 474 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 476
                self.operand()
                self.state = 478 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 477
                        self.array_access_box()

                    else:
                        raise NoViableAltException(self)
                    self.state = 480 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def OPEN_BRACE(self):
            return self.getToken(MiniGoParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(MiniGoParser.CLOSE_BRACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def struct_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Struct_fieldContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Struct_fieldContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_decl" ):
                return visitor.visitStruct_decl(self)
            else:
                return visitor.visitChildren(self)




    def struct_decl(self):

        localctx = MiniGoParser.Struct_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_struct_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self.match(MiniGoParser.TYPE)
            self.state = 485
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 486
            self.match(MiniGoParser.STRUCT)
            self.state = 487
            self.match(MiniGoParser.OPEN_BRACE)
            self.state = 489 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 488
                self.struct_field()
                self.state = 491 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.IDENTIFIER):
                    break

            self.state = 493
            self.match(MiniGoParser.CLOSE_BRACE)
            self.state = 494
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_field" ):
                return visitor.visitStruct_field(self)
            else:
                return visitor.visitChildren(self)




    def struct_field(self):

        localctx = MiniGoParser.Struct_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_struct_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 497
            self.typ()
            self.state = 498
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def OPEN_BRACE(self):
            return self.getToken(MiniGoParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(MiniGoParser.CLOSE_BRACE, 0)

        def struct_ele_list(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_ele_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_struct_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 501
            self.match(MiniGoParser.OPEN_BRACE)
            self.state = 503
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 502
                self.struct_ele_list()


            self.state = 505
            self.match(MiniGoParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_ele_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_ele(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Struct_eleContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Struct_eleContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_ele_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_ele_list" ):
                return visitor.visitStruct_ele_list(self)
            else:
                return visitor.visitChildren(self)




    def struct_ele_list(self):

        localctx = MiniGoParser.Struct_ele_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_struct_ele_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.struct_ele()
            self.state = 512
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 508
                self.match(MiniGoParser.COMMA)
                self.state = 509
                self.struct_ele()
                self.state = 514
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_eleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_ele

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_ele" ):
                return visitor.visitStruct_ele(self)
            else:
                return visitor.visitChildren(self)




    def struct_ele(self):

        localctx = MiniGoParser.Struct_eleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_struct_ele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 516
            self.match(MiniGoParser.COLON)
            self.state = 517
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_array_method(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_array_methodContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_access" ):
                return visitor.visitStruct_access(self)
            else:
                return visitor.visitChildren(self)




    def struct_access(self):

        localctx = MiniGoParser.Struct_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_struct_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self.struct_array_method()
            self.state = 520
            self.match(MiniGoParser.DOT)
            self.state = 521
            self.match(MiniGoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_array_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(MiniGoParser.OperandContext,0)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.DOT)
            else:
                return self.getToken(MiniGoParser.DOT, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def func_call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Func_callContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Func_callContext,i)


        def array_access_box(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_access_boxContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_access_boxContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_array_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_array_method" ):
                return visitor.visitStruct_array_method(self)
            else:
                return visitor.visitChildren(self)




    def struct_array_method(self):

        localctx = MiniGoParser.Struct_array_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_struct_array_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.operand()
            self.state = 535
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 533
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                    if la_ == 1:
                        self.state = 524
                        self.match(MiniGoParser.DOT)
                        self.state = 525
                        self.match(MiniGoParser.IDENTIFIER)
                        pass

                    elif la_ == 2:
                        self.state = 527 
                        self._errHandler.sync(self)
                        _alt = 1
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt == 1:
                                self.state = 526
                                self.array_access_box()

                            else:
                                raise NoViableAltException(self)
                            self.state = 529 
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

                        pass

                    elif la_ == 3:
                        self.state = 531
                        self.match(MiniGoParser.DOT)
                        self.state = 532
                        self.func_call()
                        pass

             
                self.state = 537
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def OPEN_BRACE(self):
            return self.getToken(MiniGoParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(MiniGoParser.CLOSE_BRACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def interface_method(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Interface_methodContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Interface_methodContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_decl" ):
                return visitor.visitInterface_decl(self)
            else:
                return visitor.visitChildren(self)




    def interface_decl(self):

        localctx = MiniGoParser.Interface_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_interface_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            self.match(MiniGoParser.TYPE)
            self.state = 539
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 540
            self.match(MiniGoParser.INTERFACE)
            self.state = 541
            self.match(MiniGoParser.OPEN_BRACE)
            self.state = 543 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 542
                self.interface_method()
                self.state = 545 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.IDENTIFIER):
                    break

            self.state = 547
            self.match(MiniGoParser.CLOSE_BRACE)
            self.state = 548
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def OPEN_PARENTHESIS(self):
            return self.getToken(MiniGoParser.OPEN_PARENTHESIS, 0)

        def CLOSE_PARENTHESIS(self):
            return self.getToken(MiniGoParser.CLOSE_PARENTHESIS, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def param_list(self):
            return self.getTypedRuleContext(MiniGoParser.Param_listContext,0)


        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method" ):
                return visitor.visitInterface_method(self)
            else:
                return visitor.visitChildren(self)




    def interface_method(self):

        localctx = MiniGoParser.Interface_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_interface_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 551
            self.match(MiniGoParser.OPEN_PARENTHESIS)
            self.state = 553
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 552
                self.param_list()


            self.state = 555
            self.match(MiniGoParser.CLOSE_PARENTHESIS)
            self.state = 557
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.OPEN_BRACKET) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 556
                self.typ()


            self.state = 559
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Param_declContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Param_declContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = MiniGoParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            self.param_decl()
            self.state = 566
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 562
                self.match(MiniGoParser.COMMA)
                self.state = 563
                self.param_decl()
                self.state = 568
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_param_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_decl" ):
                return visitor.visitParam_decl(self)
            else:
                return visitor.visitChildren(self)




    def param_decl(self):

        localctx = MiniGoParser.Param_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_param_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 574
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 570
                self.match(MiniGoParser.COMMA)
                self.state = 571
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 576
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 577
            self.typ()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arith_high_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULTIPLY(self):
            return self.getToken(MiniGoParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(MiniGoParser.DIVIDE, 0)

        def REMAIN(self):
            return self.getToken(MiniGoParser.REMAIN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arith_high_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArith_high_operator" ):
                return visitor.visitArith_high_operator(self)
            else:
                return visitor.visitChildren(self)




    def arith_high_operator(self):

        localctx = MiniGoParser.Arith_high_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_arith_high_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 579
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MULTIPLY) | (1 << MiniGoParser.DIVIDE) | (1 << MiniGoParser.REMAIN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arith_low_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arith_low_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArith_low_operator" ):
                return visitor.visitArith_low_operator(self)
            else:
                return visitor.visitChildren(self)




    def arith_low_operator(self):

        localctx = MiniGoParser.Arith_low_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_arith_low_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMPARE_STR(self):
            return self.getToken(MiniGoParser.COMPARE_STR, 0)

        def NOT_EQ(self):
            return self.getToken(MiniGoParser.NOT_EQ, 0)

        def GREATER_OR_EQ(self):
            return self.getToken(MiniGoParser.GREATER_OR_EQ, 0)

        def LESS_OR_EQ(self):
            return self.getToken(MiniGoParser.LESS_OR_EQ, 0)

        def GREATER(self):
            return self.getToken(MiniGoParser.GREATER, 0)

        def LESS(self):
            return self.getToken(MiniGoParser.LESS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_relational_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_operator" ):
                return visitor.visitRelational_operator(self)
            else:
                return visitor.visitChildren(self)




    def relational_operator(self):

        localctx = MiniGoParser.Relational_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_relational_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 583
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.COMPARE_STR) | (1 << MiniGoParser.NOT_EQ) | (1 << MiniGoParser.GREATER_OR_EQ) | (1 << MiniGoParser.LESS_OR_EQ) | (1 << MiniGoParser.GREATER) | (1 << MiniGoParser.LESS))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGNMENT_SIGN(self):
            return self.getToken(MiniGoParser.ASSIGNMENT_SIGN, 0)

        def SHORT_ADD(self):
            return self.getToken(MiniGoParser.SHORT_ADD, 0)

        def SHORT_SUB(self):
            return self.getToken(MiniGoParser.SHORT_SUB, 0)

        def SHORT_MULTIPLY(self):
            return self.getToken(MiniGoParser.SHORT_MULTIPLY, 0)

        def SHORT_DIVIDE(self):
            return self.getToken(MiniGoParser.SHORT_DIVIDE, 0)

        def SHORT_REMAIN(self):
            return self.getToken(MiniGoParser.SHORT_REMAIN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_operator" ):
                return visitor.visitAssign_operator(self)
            else:
                return visitor.visitChildren(self)




    def assign_operator(self):

        localctx = MiniGoParser.Assign_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_assign_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGNMENT_SIGN) | (1 << MiniGoParser.SHORT_ADD) | (1 << MiniGoParser.SHORT_SUB) | (1 << MiniGoParser.SHORT_MULTIPLY) | (1 << MiniGoParser.SHORT_DIVIDE) | (1 << MiniGoParser.SHORT_REMAIN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLE_LINE_COMMENT(self):
            return self.getToken(MiniGoParser.SINGLE_LINE_COMMENT, 0)

        def MULTI_LINE_COMMENT(self):
            return self.getToken(MiniGoParser.MULTI_LINE_COMMENT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_comment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = MiniGoParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 587
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SINGLE_LINE_COMMENT or _la==MiniGoParser.MULTI_LINE_COMMENT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[29] = self.expr_sempred
        self._predicates[30] = self.expr1_sempred
        self._predicates[31] = self.expr2_sempred
        self._predicates[32] = self.expr3_sempred
        self._predicates[33] = self.expr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




