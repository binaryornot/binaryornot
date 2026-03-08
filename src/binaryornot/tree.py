"""Auto-generated decision tree for binary/text classification.

Do not edit by hand. Regenerate with:
    uv run --with 'scikit-learn,numpy,hypothesis' python scripts/train_detector.py
"""


def is_binary(features):
    """Classify a byte chunk as binary or text.

    Takes the feature list from helpers._compute_features().
    Returns True for binary.
    """
    if features[1] <= 0.000977:  # control_ratio
        if features[17] <= 0.000977:  # longest_printable_run
            if features[4] <= 0.500000:  # utf8_valid
                if features[22] <= 0.500000:  # try_euc_kr
                    if features[7] <= 1.953445:  # byte_entropy
                        return True  # binary (100.0%, n=1)
                    else:
                        if features[7] <= 2.749470:  # byte_entropy
                            return False  # text (100.0%, n=1)
                        else:
                            if features[14] <= 0.500000:  # try_utf16be
                                return True  # binary (100.0%, n=1)
                            else:
                                return True  # binary (100.0%, n=1)
                else:
                    return False  # text (100.0%, n=1)
            else:
                return False  # text (100.0%, n=1)
        else:
            if features[4] <= 0.500000:  # utf8_valid
                if features[17] <= 0.063636:  # longest_printable_run
                    if features[7] <= 2.021329:  # byte_entropy
                        return True  # binary (100.0%, n=1)
                    else:
                        if features[13] <= 0.500000:  # try_utf16le
                            return False  # text (100.0%, n=1)
                        else:
                            return False  # text (100.0%, n=1)
                else:
                    if features[7] <= 3.047898:  # byte_entropy
                        return False  # text (100.0%, n=1)
                    else:
                        if features[2] <= 0.758706:  # printable_ascii_ratio
                            if features[17] <= 0.134848:  # longest_printable_run
                                if features[3] <= 0.633612:  # high_byte_ratio
                                    if features[7] <= 3.851786:  # byte_entropy
                                        return False  # text (100.0%, n=1)
                                    else:
                                        if features[3] <= 0.483333:  # high_byte_ratio
                                            return False  # text (100.0%, n=1)
                                        else:
                                            if features[17] <= 0.129167:  # longest_printable_run
                                                return True  # binary (100.0%, n=1)
                                            else:
                                                return False  # text (100.0%, n=1)
                                else:
                                    if features[2] <= 0.145455:  # printable_ascii_ratio
                                        return False  # text (100.0%, n=1)
                                    else:
                                        return True  # binary (100.0%, n=1)
                            else:
                                if features[19] <= 0.500000:  # try_big5
                                    if features[7] <= 3.572021:  # byte_entropy
                                        if features[3] <= 0.490000:  # high_byte_ratio
                                            if features[2] <= 0.651515:  # printable_ascii_ratio
                                                return False  # text (100.0%, n=1)
                                            else:
                                                return True  # binary (100.0%, n=1)
                                        else:
                                            if features[7] <= 3.370112:  # byte_entropy
                                                return True  # binary (100.0%, n=1)
                                            else:
                                                if features[3] <= 0.651515:  # high_byte_ratio
                                                    if features[17] <= 0.318182:  # longest_printable_run
                                                        return True  # binary (58.3%, n=1)
                                                    else:
                                                        return True  # binary (100.0%, n=1)
                                                else:
                                                    return True  # binary (100.0%, n=1)
                                    else:
                                        if features[2] <= 0.615079:  # printable_ascii_ratio
                                            if features[20] <= 0.500000:  # try_shift_jis
                                                if features[13] <= 0.500000:  # try_utf16le
                                                    return True  # binary (100.0%, n=1)
                                                else:
                                                    return True  # binary (100.0%, n=1)
                                            else:
                                                if features[17] <= 0.176923:  # longest_printable_run
                                                    return False  # text (100.0%, n=1)
                                                else:
                                                    return True  # binary (100.0%, n=1)
                                        else:
                                            if features[17] <= 0.252381:  # longest_printable_run
                                                return False  # text (100.0%, n=1)
                                            else:
                                                return True  # binary (100.0%, n=1)
                                else:
                                    if features[7] <= 3.889752:  # byte_entropy
                                        return True  # binary (100.0%, n=1)
                                    else:
                                        return False  # text (100.0%, n=1)
                        else:
                            return False  # text (100.0%, n=1)
            else:
                return False  # text (100.0%, n=1)
    else:
        if features[0] <= 0.163978:  # null_ratio
            if features[4] <= 0.500000:  # utf8_valid
                if features[7] <= 3.264621:  # byte_entropy
                    if features[17] <= 0.022678:  # longest_printable_run
                        if features[2] <= 0.000977:  # printable_ascii_ratio
                            if features[5] <= 0.001953:  # even_null_ratio
                                return False  # text (100.0%, n=1)
                            else:
                                return True  # binary (100.0%, n=1)
                        else:
                            return True  # binary (100.0%, n=1)
                    else:
                        if features[1] <= 0.095455:  # control_ratio
                            if features[17] <= 0.306818:  # longest_printable_run
                                if features[1] <= 0.055728:  # control_ratio
                                    return False  # text (100.0%, n=1)
                                else:
                                    return False  # text (100.0%, n=1)
                            else:
                                return True  # binary (100.0%, n=1)
                        else:
                            return False  # text (100.0%, n=1)
                else:
                    if features[10] <= 0.500000:  # bom_utf16le
                        if features[2] <= 0.455534:  # printable_ascii_ratio
                            if features[3] <= 0.790570:  # high_byte_ratio
                                if features[1] <= 0.485714:  # control_ratio
                                    if features[7] <= 3.540884:  # byte_entropy
                                        if features[7] <= 3.528408:  # byte_entropy
                                            if features[2] <= 0.316667:  # printable_ascii_ratio
                                                if features[2] <= 0.286364:  # printable_ascii_ratio
                                                    if features[17] <= 0.095455:  # longest_printable_run
                                                        return True  # binary (87.5%, n=0)
                                                    else:
                                                        return True  # binary (100.0%, n=1)
                                                else:
                                                    if features[13] <= 0.500000:  # try_utf16le
                                                        return False  # text (100.0%, n=1)
                                                    else:
                                                        return True  # binary (100.0%, n=1)
                                            else:
                                                return True  # binary (100.0%, n=1)
                                        else:
                                            return False  # text (100.0%, n=1)
                                    else:
                                        if features[2] <= 0.446657:  # printable_ascii_ratio
                                            return True  # binary (100.0%, n=1)
                                        else:
                                            if features[17] <= 0.066638:  # longest_printable_run
                                                if features[2] <= 0.450099:  # printable_ascii_ratio
                                                    return False  # text (100.0%, n=1)
                                                else:
                                                    return True  # binary (100.0%, n=1)
                                            else:
                                                return True  # binary (100.0%, n=1)
                                else:
                                    return False  # text (100.0%, n=1)
                            else:
                                return False  # text (100.0%, n=1)
                        else:
                            if features[3] <= 0.425959:  # high_byte_ratio
                                if features[3] <= 0.394552:  # high_byte_ratio
                                    if features[7] <= 4.209417:  # byte_entropy
                                        if features[7] <= 4.175213:  # byte_entropy
                                            if features[3] <= 0.100962:  # high_byte_ratio
                                                return False  # text (100.0%, n=1)
                                            else:
                                                if features[3] <= 0.248047:  # high_byte_ratio
                                                    return True  # binary (100.0%, n=1)
                                                else:
                                                    if features[17] <= 0.106443:  # longest_printable_run
                                                        return False  # text (100.0%, n=1)
                                                    else:
                                                        return True  # binary (92.9%, n=1)
                                        else:
                                            return False  # text (100.0%, n=1)
                                    else:
                                        if features[23] <= 0.500000:  # has_magic_signature
                                            return True  # binary (100.0%, n=1)
                                        else:
                                            return True  # binary (100.0%, n=1)
                                else:
                                    if features[17] <= 0.082906:  # longest_printable_run
                                        return False  # text (100.0%, n=1)
                                    else:
                                        if features[1] <= 0.025000:  # control_ratio
                                            return False  # text (100.0%, n=1)
                                        else:
                                            if features[7] <= 3.520764:  # byte_entropy
                                                return False  # text (100.0%, n=1)
                                            else:
                                                if features[1] <= 0.122500:  # control_ratio
                                                    return True  # binary (100.0%, n=1)
                                                else:
                                                    if features[0] <= 0.033333:  # null_ratio
                                                        return False  # text (100.0%, n=1)
                                                    else:
                                                        return True  # binary (100.0%, n=1)
                            else:
                                if features[17] <= 0.098599:  # longest_printable_run
                                    if features[1] <= 0.012902:  # control_ratio
                                        return True  # binary (100.0%, n=1)
                                    else:
                                        if features[23] <= 0.500000:  # has_magic_signature
                                            return False  # text (100.0%, n=1)
                                        else:
                                            if features[3] <= 0.458087:  # high_byte_ratio
                                                return True  # binary (100.0%, n=1)
                                            else:
                                                return True  # binary (100.0%, n=1)
                                else:
                                    if features[7] <= 4.453697:  # byte_entropy
                                        if features[3] <= 0.472136:  # high_byte_ratio
                                            if features[17] <= 0.121324:  # longest_printable_run
                                                return False  # text (100.0%, n=1)
                                            else:
                                                if features[17] <= 0.302885:  # longest_printable_run
                                                    if features[7] <= 3.539612:  # byte_entropy
                                                        return False  # text (100.0%, n=1)
                                                    else:
                                                        return True  # binary (100.0%, n=1)
                                                else:
                                                    return False  # text (100.0%, n=1)
                                        else:
                                            return True  # binary (100.0%, n=1)
                                    else:
                                        return True  # binary (100.0%, n=1)
                    else:
                        if features[14] <= 0.500000:  # try_utf16be
                            return False  # text (100.0%, n=1)
                        else:
                            return False  # text (100.0%, n=1)
            else:
                if features[1] <= 0.450000:  # control_ratio
                    if features[1] <= 0.006212:  # control_ratio
                        return True  # binary (100.0%, n=1)
                    else:
                        return False  # text (100.0%, n=1)
                else:
                    return True  # binary (100.0%, n=1)
        else:
            if features[23] <= 0.500000:  # has_magic_signature
                if features[3] <= 0.082843:  # high_byte_ratio
                    if features[6] <= 0.282534:  # odd_null_ratio
                        return False  # text (100.0%, n=1)
                    else:
                        if features[7] <= 3.088801:  # byte_entropy
                            if features[0] <= 0.822852:  # null_ratio
                                if features[2] <= 0.291667:  # printable_ascii_ratio
                                    return False  # text (100.0%, n=1)
                                else:
                                    if features[1] <= 0.521739:  # control_ratio
                                        return False  # text (100.0%, n=1)
                                    else:
                                        return True  # binary (100.0%, n=1)
                            else:
                                if features[16] <= 0.500000:  # try_utf32be
                                    return True  # binary (100.0%, n=1)
                                else:
                                    return True  # binary (100.0%, n=1)
                        else:
                            if features[5] <= 0.140625:  # even_null_ratio
                                return False  # text (100.0%, n=1)
                            else:
                                return True  # binary (100.0%, n=1)
                else:
                    if features[17] <= 0.291667:  # longest_printable_run
                        if features[7] <= 0.698576:  # byte_entropy
                            return True  # binary (100.0%, n=1)
                        else:
                            if features[7] <= 5.613847:  # byte_entropy
                                if features[2] <= 0.361264:  # printable_ascii_ratio
                                    if features[20] <= 0.500000:  # try_shift_jis
                                        return False  # text (100.0%, n=1)
                                    else:
                                        if features[14] <= 0.500000:  # try_utf16be
                                            if features[0] <= 0.379808:  # null_ratio
                                                return False  # text (100.0%, n=1)
                                            else:
                                                return True  # binary (100.0%, n=1)
                                        else:
                                            return False  # text (100.0%, n=1)
                                else:
                                    if features[2] <= 0.408333:  # printable_ascii_ratio
                                        if features[1] <= 0.260000:  # control_ratio
                                            return False  # text (100.0%, n=1)
                                        else:
                                            return True  # binary (100.0%, n=1)
                                    else:
                                        return False  # text (100.0%, n=1)
                            else:
                                if features[17] <= 0.012485:  # longest_printable_run
                                    return False  # text (100.0%, n=1)
                                else:
                                    return True  # binary (100.0%, n=1)
                    else:
                        return True  # binary (100.0%, n=1)
            else:
                if features[20] <= 0.500000:  # try_shift_jis
                    return True  # binary (100.0%, n=1)
                else:
                    return True  # binary (100.0%, n=1)
