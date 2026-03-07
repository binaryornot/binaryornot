"""Auto-generated decision tree for binary/text classification.

Do not edit by hand. Regenerate with:
    uv run --with 'scikit-learn,numpy,hypothesis' python scripts/train_detector.py
"""


def is_binary(features):
    """Classify a byte chunk as binary or text.

    Takes the feature list from helpers._compute_features().
    Returns True for binary.
    """
    if features[7] <= 3.457998:  # byte_entropy
        if features[1] <= 0.796165:  # control_ratio
            if features[3] <= 0.972656:  # high_byte_ratio
                if features[7] <= 3.041395:  # byte_entropy
                    if features[1] <= 0.753906:  # control_ratio
                        if features[0] <= 0.712912:  # null_ratio
                            return False  # text (100.0%, n=1)
                        else:
                            if features[0] <= 0.716518:  # null_ratio
                                if features[2] <= 0.089286:  # printable_ascii_ratio
                                    return False  # text (100.0%, n=1)
                                else:
                                    return True  # binary (100.0%, n=1)
                            else:
                                return False  # text (100.0%, n=1)
                    else:
                        if features[2] <= 0.180990:  # printable_ascii_ratio
                            return False  # text (100.0%, n=1)
                        else:
                            return True  # binary (100.0%, n=1)
                else:
                    if features[7] <= 3.092967:  # byte_entropy
                        if features[5] <= 0.023438:  # even_null_ratio
                            if features[1] <= 0.652778:  # control_ratio
                                return False  # text (100.0%, n=1)
                            else:
                                return True  # binary (100.0%, n=1)
                        else:
                            if features[6] <= 0.562500:  # odd_null_ratio
                                if features[6] <= 0.031250:  # odd_null_ratio
                                    return False  # text (100.0%, n=1)
                                else:
                                    return True  # binary (100.0%, n=1)
                            else:
                                return False  # text (100.0%, n=1)
                    else:
                        if features[17] <= 0.154762:  # longest_printable_run
                            if features[17] <= 0.003906:  # longest_printable_run
                                if features[4] <= 0.500000:  # utf8_valid
                                    if features[1] <= 0.316667:  # control_ratio
                                        return True  # binary (100.0%, n=1)
                                    else:
                                        return False  # text (100.0%, n=1)
                                else:
                                    return False  # text (100.0%, n=1)
                            else:
                                if features[17] <= 0.080128:  # longest_printable_run
                                    if features[20] <= 0.500000:  # try_shift_jis
                                        return False  # text (100.0%, n=1)
                                    else:
                                        if features[17] <= 0.027043:  # longest_printable_run
                                            return False  # text (100.0%, n=1)
                                        else:
                                            return True  # binary (100.0%, n=1)
                                else:
                                    if features[1] <= 0.150000:  # control_ratio
                                        if features[4] <= 0.500000:  # utf8_valid
                                            if features[7] <= 3.145926:  # byte_entropy
                                                return True  # binary (100.0%, n=1)
                                            else:
                                                if features[1] <= 0.085714:  # control_ratio
                                                    return False  # text (100.0%, n=1)
                                                else:
                                                    if features[1] <= 0.105556:  # control_ratio
                                                        return True  # binary (100.0%, n=1)
                                                    else:
                                                        return False  # text (100.0%, n=1)
                                        else:
                                            return False  # text (100.0%, n=1)
                                    else:
                                        if features[0] <= 0.100000:  # null_ratio
                                            if features[3] <= 0.381818:  # high_byte_ratio
                                                return False  # text (100.0%, n=1)
                                            else:
                                                if features[2] <= 0.236364:  # printable_ascii_ratio
                                                    return False  # text (100.0%, n=1)
                                                else:
                                                    return True  # binary (100.0%, n=1)
                                        else:
                                            return False  # text (100.0%, n=1)
                        else:
                            if features[4] <= 0.500000:  # utf8_valid
                                if features[7] <= 3.264621:  # byte_entropy
                                    if features[17] <= 0.174242:  # longest_printable_run
                                        return False  # text (100.0%, n=1)
                                    else:
                                        if features[1] <= 0.095455:  # control_ratio
                                            if features[2] <= 0.618182:  # printable_ascii_ratio
                                                return True  # binary (100.0%, n=1)
                                            else:
                                                return False  # text (100.0%, n=1)
                                        else:
                                            return False  # text (100.0%, n=1)
                                else:
                                    if features[1] <= 0.041667:  # control_ratio
                                        if features[2] <= 0.416667:  # printable_ascii_ratio
                                            return True  # binary (100.0%, n=1)
                                        else:
                                            if features[7] <= 3.398540:  # byte_entropy
                                                return False  # text (100.0%, n=1)
                                            else:
                                                if features[2] <= 0.583333:  # printable_ascii_ratio
                                                    return False  # text (50.0%, n=1)
                                                else:
                                                    return True  # binary (100.0%, n=1)
                                    else:
                                        if features[3] <= 0.591667:  # high_byte_ratio
                                            return True  # binary (100.0%, n=1)
                                        else:
                                            return False  # text (100.0%, n=1)
                            else:
                                if features[6] <= 0.178571:  # odd_null_ratio
                                    return False  # text (100.0%, n=1)
                                else:
                                    return True  # binary (100.0%, n=1)
            else:
                if features[4] <= 0.500000:  # utf8_valid
                    if features[7] <= 1.753445:  # byte_entropy
                        return True  # binary (100.0%, n=1)
                    else:
                        if features[7] <= 2.860666:  # byte_entropy
                            return False  # text (100.0%, n=1)
                        else:
                            if features[20] <= 0.500000:  # try_shift_jis
                                return True  # binary (100.0%, n=1)
                            else:
                                return False  # text (50.0%, n=1)
                else:
                    return False  # text (100.0%, n=1)
        else:
            if features[3] <= 0.048438:  # high_byte_ratio
                if features[5] <= 0.962963:  # even_null_ratio
                    return True  # binary (100.0%, n=1)
                else:
                    if features[6] <= 0.800000:  # odd_null_ratio
                        return False  # text (100.0%, n=1)
                    else:
                        return True  # binary (100.0%, n=1)
            else:
                if features[0] <= 0.791667:  # null_ratio
                    return False  # text (100.0%, n=1)
                else:
                    return True  # binary (100.0%, n=1)
    else:
        if features[4] <= 0.500000:  # utf8_valid
            if features[17] <= 0.045663:  # longest_printable_run
                if features[7] <= 5.183908:  # byte_entropy
                    if features[2] <= 0.007812:  # printable_ascii_ratio
                        return True  # binary (100.0%, n=1)
                    else:
                        if features[1] <= 0.575621:  # control_ratio
                            if features[17] <= 0.041452:  # longest_printable_run
                                return False  # text (100.0%, n=1)
                            else:
                                if features[7] <= 4.408838:  # byte_entropy
                                    return False  # text (100.0%, n=1)
                                else:
                                    if features[2] <= 0.426660:  # printable_ascii_ratio
                                        return True  # binary (100.0%, n=1)
                                    else:
                                        return False  # text (100.0%, n=1)
                        else:
                            return True  # binary (100.0%, n=1)
                else:
                    if features[2] <= 0.476415:  # printable_ascii_ratio
                        return True  # binary (100.0%, n=1)
                    else:
                        return False  # text (100.0%, n=1)
            else:
                if features[1] <= 0.029040:  # control_ratio
                    if features[17] <= 0.354353:  # longest_printable_run
                        if features[2] <= 0.615079:  # printable_ascii_ratio
                            if features[19] <= 0.500000:  # try_big5
                                if features[17] <= 0.082207:  # longest_printable_run
                                    if features[2] <= 0.348718:  # printable_ascii_ratio
                                        return True  # binary (100.0%, n=1)
                                    else:
                                        return False  # text (100.0%, n=1)
                                else:
                                    if features[2] <= 0.458042:  # printable_ascii_ratio
                                        if features[17] <= 0.261364:  # longest_printable_run
                                            return True  # binary (100.0%, n=1)
                                        else:
                                            return False  # text (100.0%, n=1)
                                    else:
                                        if features[17] <= 0.163333:  # longest_printable_run
                                            if features[7] <= 4.704511:  # byte_entropy
                                                if features[3] <= 0.490000:  # high_byte_ratio
                                                    return False  # text (100.0%, n=1)
                                                else:
                                                    if features[7] <= 3.890945:  # byte_entropy
                                                        return True  # binary (100.0%, n=1)
                                                    else:
                                                        return False  # text (100.0%, n=1)
                                            else:
                                                return True  # binary (100.0%, n=1)
                                        else:
                                            return True  # binary (100.0%, n=1)
                            else:
                                return False  # text (100.0%, n=1)
                        else:
                            if features[7] <= 3.921242:  # byte_entropy
                                if features[17] <= 0.207407:  # longest_printable_run
                                    return False  # text (100.0%, n=1)
                                else:
                                    return True  # binary (100.0%, n=1)
                            else:
                                return False  # text (100.0%, n=1)
                    else:
                        return True  # binary (100.0%, n=1)
                else:
                    if features[10] <= 0.500000:  # bom_utf16le
                        if features[11] <= 0.500000:  # bom_utf16be
                            if features[6] <= 0.499089:  # odd_null_ratio
                                if features[7] <= 4.385591:  # byte_entropy
                                    if features[17] <= 0.097619:  # longest_printable_run
                                        if features[2] <= 0.459416:  # printable_ascii_ratio
                                            if features[0] <= 0.116667:  # null_ratio
                                                if features[2] <= 0.404762:  # printable_ascii_ratio
                                                    if features[1] <= 0.261364:  # control_ratio
                                                        return True  # binary (100.0%, n=1)
                                                    else:
                                                        return False  # text (50.0%, n=1)
                                                else:
                                                    if features[2] <= 0.450957:  # printable_ascii_ratio
                                                        return False  # text (66.7%, n=1)
                                                    else:
                                                        return True  # binary (100.0%, n=1)
                                            else:
                                                return False  # text (100.0%, n=1)
                                        else:
                                            return False  # text (100.0%, n=1)
                                    else:
                                        if features[2] <= 0.651515:  # printable_ascii_ratio
                                            if features[2] <= 0.456439:  # printable_ascii_ratio
                                                return True  # binary (100.0%, n=1)
                                            else:
                                                if features[2] <= 0.459936:  # printable_ascii_ratio
                                                    return False  # text (100.0%, n=1)
                                                else:
                                                    if features[17] <= 0.174242:  # longest_printable_run
                                                        return True  # binary (75.0%, n=1)
                                                    else:
                                                        return True  # binary (95.0%, n=1)
                                        else:
                                            return False  # text (100.0%, n=1)
                                else:
                                    if features[1] <= 0.042572:  # control_ratio
                                        if features[3] <= 0.446360:  # high_byte_ratio
                                            if features[17] <= 0.109762:  # longest_printable_run
                                                return False  # text (100.0%, n=1)
                                            else:
                                                return True  # binary (100.0%, n=1)
                                        else:
                                            return True  # binary (100.0%, n=1)
                                    else:
                                        if features[17] <= 0.055947:  # longest_printable_run
                                            if features[2] <= 0.439236:  # printable_ascii_ratio
                                                return True  # binary (100.0%, n=1)
                                            else:
                                                return False  # text (100.0%, n=1)
                                        else:
                                            return True  # binary (100.0%, n=1)
                            else:
                                return False  # text (100.0%, n=1)
                        else:
                            return False  # text (100.0%, n=1)
                    else:
                        return False  # text (100.0%, n=1)
        else:
            if features[1] <= 0.655405:  # control_ratio
                return False  # text (100.0%, n=1)
            else:
                return True  # binary (100.0%, n=1)
