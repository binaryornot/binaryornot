"""Auto-generated decision tree for binary/text classification.

Do not edit by hand. Regenerate with:
    uv run --with 'scikit-learn,numpy,hypothesis' python scripts/train_detector.py
"""


def is_binary(features):
    """Classify a byte chunk as binary or text.

    Takes the feature list from helpers._compute_features().
    Returns True for binary.
    """
    if features[7] <= 3.584487:  # byte_entropy
        if features[7] <= 1.091603:  # byte_entropy
            if features[17] <= 0.208333:  # longest_printable_run
                if features[14] <= 0.500000:  # try_utf16be
                    if features[5] <= 0.250000:  # even_null_ratio
                        return True  # binary (100.0%, n=1)
                    else:
                        if features[21] <= 0.500000:  # try_euc_jp
                            return False  # text (100.0%, n=1)
                        else:
                            return True  # binary (100.0%, n=1)
                else:
                    return True  # binary (100.0%, n=1)
            else:
                return False  # text (100.0%, n=1)
        else:
            if features[0] <= 0.101010:  # null_ratio
                if features[1] <= 0.023438:  # control_ratio
                    if features[17] <= 0.003378:  # longest_printable_run
                        if features[4] <= 0.500000:  # utf8_valid
                            if features[7] <= 1.953445:  # byte_entropy
                                return True  # binary (100.0%, n=1)
                            else:
                                if features[7] <= 2.860666:  # byte_entropy
                                    return False  # text (100.0%, n=1)
                                else:
                                    return True  # binary (100.0%, n=1)
                        else:
                            return False  # text (100.0%, n=1)
                    else:
                        if features[4] <= 0.500000:  # utf8_valid
                            if features[7] <= 3.047898:  # byte_entropy
                                return False  # text (100.0%, n=1)
                            else:
                                if features[17] <= 0.174242:  # longest_printable_run
                                    if features[3] <= 0.584848:  # high_byte_ratio
                                        return False  # text (93.8%, n=1)
                                    else:
                                        return True  # binary (100.0%, n=1)
                                else:
                                    if features[3] <= 0.464286:  # high_byte_ratio
                                        return True  # binary (66.7%, n=1)
                                    else:
                                        return True  # binary (100.0%, n=1)
                        else:
                            return False  # text (100.0%, n=1)
                else:
                    if features[7] <= 2.840248:  # byte_entropy
                        if features[22] <= 0.500000:  # try_euc_kr
                            return False  # text (100.0%, n=1)
                        else:
                            return True  # binary (100.0%, n=1)
                    else:
                        if features[7] <= 2.934816:  # byte_entropy
                            return True  # binary (100.0%, n=1)
                        else:
                            if features[7] <= 3.264621:  # byte_entropy
                                if features[3] <= 0.303030:  # high_byte_ratio
                                    if features[6] <= 0.083333:  # odd_null_ratio
                                        return True  # binary (83.3%, n=1)
                                    else:
                                        return False  # text (100.0%, n=1)
                                else:
                                    if features[17] <= 0.333333:  # longest_printable_run
                                        return False  # text (100.0%, n=1)
                                    else:
                                        return True  # binary (100.0%, n=1)
                            else:
                                if features[1] <= 0.074176:  # control_ratio
                                    return False  # text (100.0%, n=1)
                                else:
                                    if features[4] <= 0.500000:  # utf8_valid
                                        return True  # binary (91.5%, n=1)
                                    else:
                                        return False  # text (60.0%, n=1)
            else:
                if features[3] <= 0.025638:  # high_byte_ratio
                    if features[3] <= 0.011159:  # high_byte_ratio
                        if features[17] <= 0.215385:  # longest_printable_run
                            return False  # text (100.0%, n=1)
                        else:
                            return True  # binary (100.0%, n=1)
                    else:
                        return True  # binary (100.0%, n=1)
                else:
                    if features[17] <= 0.172619:  # longest_printable_run
                        return False  # text (100.0%, n=1)
                    else:
                        if features[20] <= 0.500000:  # try_shift_jis
                            return False  # text (100.0%, n=1)
                        else:
                            return True  # binary (100.0%, n=1)
    else:
        if features[4] <= 0.500000:  # utf8_valid
            if features[2] <= 0.236068:  # printable_ascii_ratio
                if features[0] <= 0.069444:  # null_ratio
                    if features[21] <= 0.500000:  # try_euc_jp
                        if features[7] <= 5.864853:  # byte_entropy
                            if features[17] <= 0.022943:  # longest_printable_run
                                if features[2] <= 0.039474:  # printable_ascii_ratio
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
                    if features[3] <= 0.142578:  # high_byte_ratio
                        return True  # binary (100.0%, n=1)
                    else:
                        return False  # text (100.0%, n=1)
            else:
                if features[1] <= 0.028934:  # control_ratio
                    if features[17] <= 0.288690:  # longest_printable_run
                        if features[2] <= 0.369925:  # printable_ascii_ratio
                            if features[17] <= 0.011490:  # longest_printable_run
                                return False  # text (100.0%, n=1)
                            else:
                                return True  # binary (100.0%, n=1)
                        else:
                            if features[17] <= 0.082207:  # longest_printable_run
                                return False  # text (100.0%, n=1)
                            else:
                                if features[7] <= 4.399041:  # byte_entropy
                                    if features[17] <= 0.138095:  # longest_printable_run
                                        return False  # text (80.0%, n=1)
                                    else:
                                        return True  # binary (87.5%, n=1)
                                else:
                                    if features[14] <= 0.500000:  # try_utf16be
                                        return False  # text (100.0%, n=1)
                                    else:
                                        return True  # binary (100.0%, n=1)
                    else:
                        return True  # binary (100.0%, n=1)
                else:
                    if features[10] <= 0.500000:  # bom_utf16le
                        if features[11] <= 0.500000:  # bom_utf16be
                            if features[17] <= 0.006415:  # longest_printable_run
                                return False  # text (100.0%, n=1)
                            else:
                                if features[5] <= 0.494214:  # even_null_ratio
                                    if features[2] <= 0.439780:  # printable_ascii_ratio
                                        return True  # binary (98.9%, n=1)
                                    else:
                                        return True  # binary (83.6%, n=1)
                                else:
                                    return False  # text (100.0%, n=1)
                        else:
                            return False  # text (100.0%, n=1)
                    else:
                        return False  # text (100.0%, n=1)
        else:
            if features[1] <= 0.206483:  # control_ratio
                if features[0] <= 0.044764:  # null_ratio
                    return False  # text (100.0%, n=1)
                else:
                    return True  # binary (100.0%, n=1)
            else:
                return True  # binary (100.0%, n=1)
