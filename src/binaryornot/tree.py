"""Auto-generated decision tree for binary/text classification.

Do not edit by hand. Regenerate with:
    uv run --with 'scikit-learn,numpy,hypothesis' python scripts/train_detector.py
"""


def is_binary(features):
    """Classify a byte chunk as binary or text.

    Takes the feature list from helpers._compute_features().
    Returns True for binary.
    """
    if features[7] <= 3.041395:  # byte_entropy
        if features[7] <= 1.106750:  # byte_entropy
            if features[2] <= 0.208333:  # printable_ascii_ratio
                if features[13] <= 0.500000:  # try_utf16le
                    if features[3] <= 0.625000:  # high_byte_ratio
                        return False  # text (100.0%, n=1)
                    else:
                        return True  # binary (100.0%, n=1)
                else:
                    return True  # binary (100.0%, n=1)
            else:
                return False  # text (100.0%, n=1)
        else:
            if features[1] <= 0.753906:  # control_ratio
                if features[3] <= 0.970588:  # high_byte_ratio
                    if features[7] <= 1.652807:  # byte_entropy
                        if features[7] <= 1.635238:  # byte_entropy
                            return False  # text (100.0%, n=1)
                        else:
                            return True  # binary (100.0%, n=1)
                    else:
                        if features[15] <= 0.500000:  # try_utf32le
                            return False  # text (100.0%, n=1)
                        else:
                            return False  # text (100.0%, n=1)
                else:
                    if features[7] <= 1.792481:  # byte_entropy
                        if features[7] <= 1.542481:  # byte_entropy
                            return False  # text (100.0%, n=1)
                        else:
                            return True  # binary (100.0%, n=1)
                    else:
                        if features[20] <= 0.500000:  # try_shift_jis
                            if features[13] <= 0.500000:  # try_utf16le
                                return False  # text (100.0%, n=1)
                            else:
                                return False  # text (100.0%, n=1)
                        else:
                            return True  # binary (100.0%, n=1)
            else:
                if features[3] <= 0.048438:  # high_byte_ratio
                    if features[0] <= 0.734375:  # null_ratio
                        return True  # binary (100.0%, n=1)
                    else:
                        return False  # text (100.0%, n=1)
                else:
                    return False  # text (100.0%, n=1)
    else:
        if features[4] <= 0.500000:  # utf8_valid
            if features[6] <= 0.534856:  # odd_null_ratio
                if features[17] <= 0.029857:  # longest_printable_run
                    if features[17] <= 0.003906:  # longest_printable_run
                        if features[0] <= 0.125000:  # null_ratio
                            return True  # binary (100.0%, n=1)
                        else:
                            return False  # text (100.0%, n=1)
                    else:
                        if features[7] <= 5.500731:  # byte_entropy
                            return False  # text (100.0%, n=1)
                        else:
                            return True  # binary (100.0%, n=1)
                else:
                    if features[10] <= 0.500000:  # bom_utf16le
                        if features[1] <= 0.031089:  # control_ratio
                            if features[17] <= 0.354353:  # longest_printable_run
                                if features[2] <= 0.614149:  # printable_ascii_ratio
                                    if features[17] <= 0.082207:  # longest_printable_run
                                        if features[2] <= 0.369697:  # printable_ascii_ratio
                                            if features[2] <= 0.192308:  # printable_ascii_ratio
                                                return False  # text (100.0%, n=1)
                                            else:
                                                return True  # binary (100.0%, n=1)
                                        else:
                                            return False  # text (100.0%, n=1)
                                    else:
                                        if features[17] <= 0.267943:  # longest_printable_run
                                            if features[2] <= 0.458042:  # printable_ascii_ratio
                                                if features[3] <= 0.850000:  # high_byte_ratio
                                                    if features[20] <= 0.500000:  # try_shift_jis
                                                        return True  # binary (100.0%, n=1)
                                                    else:
                                                        return True  # binary (100.0%, n=1)
                                                else:
                                                    return False  # text (100.0%, n=1)
                                            else:
                                                if features[7] <= 3.572021:  # byte_entropy
                                                    if features[7] <= 3.155913:  # byte_entropy
                                                        return True  # binary (100.0%, n=1)
                                                    else:
                                                        return False  # text (84.6%, n=1)
                                                else:
                                                    if features[17] <= 0.136111:  # longest_printable_run
                                                        return False  # text (52.4%, n=0)
                                                    else:
                                                        return True  # binary (93.6%, n=0)
                                        else:
                                            if features[2] <= 0.423810:  # printable_ascii_ratio
                                                return False  # text (100.0%, n=1)
                                            else:
                                                if features[7] <= 4.446973:  # byte_entropy
                                                    return True  # binary (100.0%, n=1)
                                                else:
                                                    return True  # binary (100.0%, n=1)
                                else:
                                    if features[13] <= 0.500000:  # try_utf16le
                                        if features[3] <= 0.348485:  # high_byte_ratio
                                            return True  # binary (100.0%, n=1)
                                        else:
                                            return False  # text (100.0%, n=1)
                                    else:
                                        return False  # text (100.0%, n=1)
                            else:
                                return True  # binary (100.0%, n=1)
                        else:
                            if features[5] <= 0.622869:  # even_null_ratio
                                if features[11] <= 0.500000:  # bom_utf16be
                                    if features[2] <= 0.146429:  # printable_ascii_ratio
                                        if features[0] <= 0.062500:  # null_ratio
                                            return True  # binary (100.0%, n=1)
                                        else:
                                            if features[7] <= 3.228202:  # byte_entropy
                                                return False  # text (100.0%, n=1)
                                            else:
                                                return False  # text (100.0%, n=1)
                                    else:
                                        if features[2] <= 0.455534:  # printable_ascii_ratio
                                            if features[7] <= 4.139454:  # byte_entropy
                                                if features[17] <= 0.038762:  # longest_printable_run
                                                    if features[20] <= 0.500000:  # try_shift_jis
                                                        return False  # text (100.0%, n=1)
                                                    else:
                                                        return True  # binary (100.0%, n=1)
                                                else:
                                                    if features[17] <= 0.114149:  # longest_printable_run
                                                        return True  # binary (85.3%, n=1)
                                                    else:
                                                        return True  # binary (97.7%, n=1)
                                            else:
                                                if features[6] <= 0.365000:  # odd_null_ratio
                                                    if features[2] <= 0.446657:  # printable_ascii_ratio
                                                        return True  # binary (100.0%, n=1)
                                                    else:
                                                        return True  # binary (97.2%, n=1)
                                                else:
                                                    return False  # text (100.0%, n=1)
                                        else:
                                            if features[17] <= 0.072300:  # longest_printable_run
                                                if features[7] <= 5.469833:  # byte_entropy
                                                    return False  # text (100.0%, n=1)
                                                else:
                                                    if features[7] <= 5.670300:  # byte_entropy
                                                        return True  # binary (100.0%, n=1)
                                                    else:
                                                        return True  # binary (100.0%, n=1)
                                            else:
                                                if features[7] <= 3.906328:  # byte_entropy
                                                    if features[1] <= 0.069048:  # control_ratio
                                                        return False  # text (100.0%, n=1)
                                                    else:
                                                        return True  # binary (86.4%, n=1)
                                                else:
                                                    if features[7] <= 4.348171:  # byte_entropy
                                                        return True  # binary (92.2%, n=1)
                                                    else:
                                                        return True  # binary (100.0%, n=1)
                                else:
                                    return False  # text (100.0%, n=1)
                            else:
                                return False  # text (100.0%, n=1)
                    else:
                        return False  # text (100.0%, n=1)
            else:
                return False  # text (100.0%, n=1)
        else:
            if features[1] <= 0.625000:  # control_ratio
                if features[5] <= 0.204887:  # even_null_ratio
                    return False  # text (100.0%, n=1)
                else:
                    if features[2] <= 0.571429:  # printable_ascii_ratio
                        return False  # text (100.0%, n=1)
                    else:
                        return True  # binary (100.0%, n=1)
            else:
                if features[7] <= 3.085009:  # byte_entropy
                    return True  # binary (100.0%, n=1)
                else:
                    return True  # binary (100.0%, n=1)
