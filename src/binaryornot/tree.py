"""Auto-generated decision tree for binary/text classification.

Do not edit by hand. Regenerate with:
    uv run --with 'scikit-learn,numpy,hypothesis' python scripts/train_detector.py
"""


def is_binary(features):
    """Classify a byte chunk as binary or text.

    Takes the feature list from helpers._compute_features().
    Returns True for binary.
    """
    if features[1] <= 0.003906:  # control_ratio
        if features[17] <= 0.003906:  # longest_printable_run
            if features[4] <= 0.500000:  # utf8_valid
                if features[19] <= 0.500000:  # try_big5
                    if features[7] <= 1.953445:  # byte_entropy
                        return True  # binary (100.0%, n=1)
                    else:
                        if features[7] <= 2.749470:  # byte_entropy
                            return False  # text (100.0%, n=1)
                        else:
                            if features[7] <= 3.004886:  # byte_entropy
                                return True  # binary (100.0%, n=1)
                            else:
                                return True  # binary (100.0%, n=1)
                else:
                    if features[21] <= 0.500000:  # try_euc_jp
                        return False  # text (100.0%, n=1)
                    else:
                        return False  # text (100.0%, n=1)
            else:
                if features[7] <= 1.750000:  # byte_entropy
                    return False  # text (100.0%, n=1)
                else:
                    return False  # text (100.0%, n=1)
        else:
            if features[4] <= 0.500000:  # utf8_valid
                if features[17] <= 0.074176:  # longest_printable_run
                    if features[7] <= 5.159404:  # byte_entropy
                        if features[7] <= 2.659421:  # byte_entropy
                            if features[7] <= 2.523218:  # byte_entropy
                                return False  # text (100.0%, n=1)
                            else:
                                return True  # binary (100.0%, n=1)
                        else:
                            return False  # text (100.0%, n=1)
                    else:
                        return True  # binary (100.0%, n=1)
                else:
                    if features[7] <= 3.040512:  # byte_entropy
                        return False  # text (100.0%, n=1)
                    else:
                        if features[17] <= 0.354353:  # longest_printable_run
                            if features[2] <= 0.615079:  # printable_ascii_ratio
                                if features[17] <= 0.267943:  # longest_printable_run
                                    if features[7] <= 3.572021:  # byte_entropy
                                        if features[3] <= 0.490000:  # high_byte_ratio
                                            return False  # text (100.0%, n=1)
                                        else:
                                            return True  # binary (66.8%, n=1)
                                    else:
                                        if features[2] <= 0.458042:  # printable_ascii_ratio
                                            return True  # binary (100.0%, n=1)
                                        else:
                                            return True  # binary (79.0%, n=0)
                                else:
                                    if features[3] <= 0.538095:  # high_byte_ratio
                                        return True  # binary (100.0%, n=1)
                                    else:
                                        return False  # text (100.0%, n=1)
                            else:
                                if features[13] <= 0.500000:  # try_utf16le
                                    if features[3] <= 0.348485:  # high_byte_ratio
                                        return True  # binary (100.0%, n=1)
                                    else:
                                        return False  # text (100.0%, n=1)
                                else:
                                    if features[17] <= 0.089844:  # longest_printable_run
                                        return False  # text (100.0%, n=1)
                                    else:
                                        return False  # text (100.0%, n=1)
                        else:
                            return True  # binary (100.0%, n=1)
            else:
                return False  # text (100.0%, n=1)
    else:
        if features[0] <= 0.163978:  # null_ratio
            if features[4] <= 0.500000:  # utf8_valid
                if features[7] <= 3.264621:  # byte_entropy
                    if features[17] <= 0.052849:  # longest_printable_run
                        if features[1] <= 0.322917:  # control_ratio
                            return True  # binary (100.0%, n=1)
                        else:
                            if features[20] <= 0.500000:  # try_shift_jis
                                return False  # text (100.0%, n=1)
                            else:
                                return True  # binary (100.0%, n=1)
                    else:
                        if features[17] <= 0.348485:  # longest_printable_run
                            return False  # text (100.0%, n=1)
                        else:
                            if features[7] <= 2.951575:  # byte_entropy
                                return False  # text (100.0%, n=1)
                            else:
                                if features[3] <= 0.303030:  # high_byte_ratio
                                    return True  # binary (100.0%, n=1)
                                else:
                                    return True  # binary (100.0%, n=1)
                else:
                    if features[1] <= 0.031089:  # control_ratio
                        if features[2] <= 0.455863:  # printable_ascii_ratio
                            return True  # binary (100.0%, n=1)
                        else:
                            if features[17] <= 0.082207:  # longest_printable_run
                                return False  # text (100.0%, n=1)
                            else:
                                if features[14] <= 0.500000:  # try_utf16be
                                    return False  # text (100.0%, n=1)
                                else:
                                    return True  # binary (100.0%, n=1)
                    else:
                        if features[10] <= 0.500000:  # bom_utf16le
                            if features[2] <= 0.455534:  # printable_ascii_ratio
                                if features[3] <= 0.790570:  # high_byte_ratio
                                    if features[17] <= 0.011719:  # longest_printable_run
                                        if features[2] <= 0.140625:  # printable_ascii_ratio
                                            return True  # binary (100.0%, n=1)
                                        else:
                                            return False  # text (100.0%, n=1)
                                    else:
                                        if features[7] <= 3.540884:  # byte_entropy
                                            return True  # binary (95.4%, n=1)
                                        else:
                                            return True  # binary (99.9%, n=1)
                                else:
                                    return False  # text (100.0%, n=1)
                            else:
                                if features[17] <= 0.072300:  # longest_printable_run
                                    if features[1] <= 0.112942:  # control_ratio
                                        if features[7] <= 5.537264:  # byte_entropy
                                            return False  # text (100.0%, n=1)
                                        else:
                                            return True  # binary (100.0%, n=1)
                                    else:
                                        return True  # binary (100.0%, n=1)
                                else:
                                    if features[7] <= 4.198218:  # byte_entropy
                                        if features[17] <= 0.174242:  # longest_printable_run
                                            return True  # binary (53.0%, n=0)
                                        else:
                                            return True  # binary (95.3%, n=1)
                                    else:
                                        if features[17] <= 0.096875:  # longest_printable_run
                                            return True  # binary (89.4%, n=0)
                                        else:
                                            return True  # binary (100.0%, n=1)
                        else:
                            return False  # text (100.0%, n=1)
            else:
                if features[1] <= 0.575000:  # control_ratio
                    return False  # text (100.0%, n=1)
                else:
                    return True  # binary (100.0%, n=1)
        else:
            if features[3] <= 0.098077:  # high_byte_ratio
                if features[8] <= 0.500000:  # bom_utf32le
                    if features[6] <= 0.125000:  # odd_null_ratio
                        return False  # text (100.0%, n=1)
                    else:
                        if features[16] <= 0.500000:  # try_utf32be
                            if features[5] <= 0.341085:  # even_null_ratio
                                return False  # text (100.0%, n=1)
                            else:
                                if features[15] <= 0.500000:  # try_utf32le
                                    if features[14] <= 0.500000:  # try_utf16be
                                        if features[7] <= 0.864787:  # byte_entropy
                                            return False  # text (100.0%, n=1)
                                        else:
                                            return True  # binary (100.0%, n=1)
                                    else:
                                        return True  # binary (100.0%, n=1)
                                else:
                                    if features[1] <= 0.925781:  # control_ratio
                                        return False  # text (100.0%, n=1)
                                    else:
                                        return True  # binary (100.0%, n=1)
                        else:
                            if features[17] <= 0.003906:  # longest_printable_run
                                return True  # binary (100.0%, n=1)
                            else:
                                return False  # text (100.0%, n=1)
                else:
                    return False  # text (100.0%, n=1)
            else:
                if features[7] <= 5.169243:  # byte_entropy
                    if features[0] <= 0.765625:  # null_ratio
                        if features[2] <= 0.378571:  # printable_ascii_ratio
                            if features[20] <= 0.500000:  # try_shift_jis
                                return False  # text (100.0%, n=1)
                            else:
                                if features[14] <= 0.500000:  # try_utf16be
                                    if features[7] <= 3.188246:  # byte_entropy
                                        return False  # text (100.0%, n=1)
                                    else:
                                        return True  # binary (100.0%, n=1)
                                else:
                                    return False  # text (100.0%, n=1)
                        else:
                            if features[13] <= 0.500000:  # try_utf16le
                                if features[3] <= 0.320000:  # high_byte_ratio
                                    return True  # binary (100.0%, n=1)
                                else:
                                    return False  # text (100.0%, n=1)
                            else:
                                if features[7] <= 2.892092:  # byte_entropy
                                    return False  # text (100.0%, n=1)
                                else:
                                    return False  # text (100.0%, n=1)
                    else:
                        if features[5] <= 0.921875:  # even_null_ratio
                            if features[2] <= 0.027344:  # printable_ascii_ratio
                                return True  # binary (100.0%, n=1)
                            else:
                                return True  # binary (100.0%, n=1)
                        else:
                            return False  # text (100.0%, n=1)
                else:
                    return True  # binary (100.0%, n=1)
