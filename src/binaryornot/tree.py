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
                if features[19] <= 0.500000:  # try_big5
                    if features[7] <= 1.953445:  # byte_entropy
                        return True  # binary (100.0%, n=1)
                    else:
                        if features[7] <= 2.749470:  # byte_entropy
                            return False  # text (100.0%, n=1)
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
                        if features[20] <= 0.500000:  # try_shift_jis
                            return False  # text (100.0%, n=1)
                        else:
                            return False  # text (100.0%, n=1)
                else:
                    if features[7] <= 3.040512:  # byte_entropy
                        return False  # text (100.0%, n=1)
                    else:
                        if features[2] <= 0.758706:  # printable_ascii_ratio
                            if features[17] <= 0.134848:  # longest_printable_run
                                if features[7] <= 3.953876:  # byte_entropy
                                    return False  # text (81.7%, n=0)
                                else:
                                    return True  # binary (87.5%, n=0)
                            else:
                                if features[19] <= 0.500000:  # try_big5
                                    return True  # binary (79.2%, n=0)
                                else:
                                    return False  # text (70.4%, n=1)
                        else:
                            return False  # text (100.0%, n=1)
            else:
                if features[18] <= 0.500000:  # try_gb2312
                    return False  # text (100.0%, n=1)
                else:
                    return False  # text (100.0%, n=1)
    else:
        if features[0] <= 0.163978:  # null_ratio
            if features[4] <= 0.500000:  # utf8_valid
                if features[7] <= 3.264621:  # byte_entropy
                    if features[17] <= 0.022678:  # longest_printable_run
                        if features[17] <= 0.000977:  # longest_printable_run
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
                                    return True  # binary (99.5%, n=1)
                                else:
                                    return False  # text (100.0%, n=1)
                            else:
                                return False  # text (100.0%, n=1)
                        else:
                            if features[3] <= 0.425959:  # high_byte_ratio
                                if features[3] <= 0.394552:  # high_byte_ratio
                                    return True  # binary (97.7%, n=0)
                                else:
                                    return True  # binary (84.4%, n=0)
                            else:
                                if features[17] <= 0.098599:  # longest_printable_run
                                    return False  # text (68.9%, n=0)
                                else:
                                    return True  # binary (86.9%, n=0)
                    else:
                        if features[1] <= 0.162500:  # control_ratio
                            return False  # text (100.0%, n=1)
                        else:
                            return False  # text (100.0%, n=1)
            else:
                if features[1] <= 0.450000:  # control_ratio
                    if features[7] <= 1.670183:  # byte_entropy
                        return True  # binary (100.0%, n=1)
                    else:
                        return False  # text (100.0%, n=1)
                else:
                    return True  # binary (100.0%, n=1)
        else:
            if features[3] <= 0.085145:  # high_byte_ratio
                if features[6] <= 0.282534:  # odd_null_ratio
                    return False  # text (100.0%, n=1)
                else:
                    if features[8] <= 0.500000:  # bom_utf32le
                        if features[5] <= 0.140625:  # even_null_ratio
                            return False  # text (100.0%, n=1)
                        else:
                            if features[16] <= 0.500000:  # try_utf32be
                                if features[15] <= 0.500000:  # try_utf32le
                                    return True  # binary (97.9%, n=1)
                                else:
                                    return False  # text (76.3%, n=0)
                            else:
                                if features[0] <= 0.879167:  # null_ratio
                                    return False  # text (100.0%, n=1)
                                else:
                                    return True  # binary (100.0%, n=1)
                    else:
                        if features[3] <= 0.004883:  # high_byte_ratio
                            return False  # text (100.0%, n=1)
                        else:
                            return False  # text (100.0%, n=1)
            else:
                if features[7] <= 4.027992:  # byte_entropy
                    if features[0] <= 0.809524:  # null_ratio
                        if features[2] <= 0.361264:  # printable_ascii_ratio
                            if features[20] <= 0.500000:  # try_shift_jis
                                return False  # text (100.0%, n=1)
                            else:
                                if features[14] <= 0.500000:  # try_utf16be
                                    return True  # binary (58.3%, n=1)
                                else:
                                    return False  # text (100.0%, n=1)
                        else:
                            if features[5] <= 0.153846:  # even_null_ratio
                                return False  # text (100.0%, n=1)
                            else:
                                return True  # binary (100.0%, n=1)
                    else:
                        if features[0] <= 0.846354:  # null_ratio
                            return True  # binary (100.0%, n=1)
                        else:
                            return True  # binary (100.0%, n=1)
                else:
                    if features[1] <= 0.457346:  # control_ratio
                        if features[7] <= 5.613847:  # byte_entropy
                            return False  # text (100.0%, n=1)
                        else:
                            if features[6] <= 0.104515:  # odd_null_ratio
                                return False  # text (100.0%, n=1)
                            else:
                                return True  # binary (100.0%, n=1)
                    else:
                        return True  # binary (100.0%, n=1)
