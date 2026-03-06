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
            if features[2] <= 0.208333:  # printable_ascii_ratio
                if features[14] <= 0.500000:  # try_utf16be
                    if features[5] <= 0.250000:  # even_null_ratio
                        return True  # binary (100.0%, n=1)
                    else:
                        if features[0] <= 0.809783:  # null_ratio
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
                                if features[7] <= 2.708618:  # byte_entropy
                                    return False  # text (100.0%, n=1)
                                else:
                                    return True  # binary (100.0%, n=1)
                        else:
                            return False  # text (100.0%, n=1)
                    else:
                        if features[4] <= 0.500000:  # utf8_valid
                            if features[7] <= 3.040512:  # byte_entropy
                                return False  # text (100.0%, n=1)
                            else:
                                if features[17] <= 0.174242:  # longest_printable_run
                                    if features[2] <= 0.415152:  # printable_ascii_ratio
                                        if features[3] <= 0.828571:  # high_byte_ratio
                                            return True  # binary (100.0%, n=1)
                                        else:
                                            return False  # text (100.0%, n=1)
                                    else:
                                        if features[17] <= 0.163333:  # longest_printable_run
                                            return False  # text (100.0%, n=1)
                                        else:
                                            if features[3] <= 0.472222:  # high_byte_ratio
                                                return False  # text (100.0%, n=1)
                                            else:
                                                return False  # text (50.0%, n=1)
                                else:
                                    if features[3] <= 0.464286:  # high_byte_ratio
                                        if features[17] <= 0.257143:  # longest_printable_run
                                            if features[14] <= 0.500000:  # try_utf16be
                                                return False  # text (50.0%, n=1)
                                            else:
                                                return False  # text (100.0%, n=1)
                                        else:
                                            return True  # binary (100.0%, n=1)
                                    else:
                                        return True  # binary (100.0%, n=1)
                        else:
                            return False  # text (100.0%, n=1)
                else:
                    if features[7] <= 2.840248:  # byte_entropy
                        if features[1] <= 0.700000:  # control_ratio
                            return False  # text (100.0%, n=1)
                        else:
                            return True  # binary (100.0%, n=1)
                    else:
                        if features[7] <= 2.934816:  # byte_entropy
                            return True  # binary (100.0%, n=1)
                        else:
                            if features[7] <= 3.264621:  # byte_entropy
                                if features[3] <= 0.303030:  # high_byte_ratio
                                    if features[10] <= 0.500000:  # bom_utf16le
                                        if features[7] <= 3.042481:  # byte_entropy
                                            return False  # text (100.0%, n=1)
                                        else:
                                            return True  # binary (100.0%, n=1)
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
                                        if features[7] <= 3.565303:  # byte_entropy
                                            if features[17] <= 0.097619:  # longest_printable_run
                                                return True  # binary (80.0%, n=1)
                                            else:
                                                return True  # binary (97.2%, n=1)
                                        else:
                                            return False  # text (100.0%, n=1)
                                    else:
                                        if features[1] <= 0.553030:  # control_ratio
                                            return False  # text (100.0%, n=1)
                                        else:
                                            return True  # binary (100.0%, n=1)
            else:
                if features[3] <= 0.022543:  # high_byte_ratio
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
                        if features[14] <= 0.500000:  # try_utf16be
                            return False  # text (100.0%, n=1)
                        else:
                            return True  # binary (100.0%, n=1)
    else:
        if features[4] <= 0.500000:  # utf8_valid
            if features[2] <= 0.236068:  # printable_ascii_ratio
                if features[0] <= 0.069444:  # null_ratio
                    if features[17] <= 0.033181:  # longest_printable_run
                        if features[2] <= 0.012821:  # printable_ascii_ratio
                            return True  # binary (100.0%, n=1)
                        else:
                            return False  # text (100.0%, n=1)
                    else:
                        return True  # binary (100.0%, n=1)
                else:
                    if features[3] <= 0.142578:  # high_byte_ratio
                        return True  # binary (100.0%, n=1)
                    else:
                        return False  # text (100.0%, n=1)
            else:
                if features[1] <= 0.005859:  # control_ratio
                    if features[17] <= 0.083333:  # longest_printable_run
                        return False  # text (100.0%, n=1)
                    else:
                        if features[7] <= 4.424946:  # byte_entropy
                            if features[3] <= 0.466063:  # high_byte_ratio
                                if features[17] <= 0.244048:  # longest_printable_run
                                    if features[7] <= 4.244984:  # byte_entropy
                                        return False  # text (100.0%, n=1)
                                    else:
                                        return True  # binary (100.0%, n=1)
                                else:
                                    return True  # binary (100.0%, n=1)
                            else:
                                if features[2] <= 0.464103:  # printable_ascii_ratio
                                    return True  # binary (100.0%, n=1)
                                else:
                                    if features[3] <= 0.531373:  # high_byte_ratio
                                        return True  # binary (100.0%, n=1)
                                    else:
                                        return False  # text (100.0%, n=1)
                        else:
                            if features[13] <= 0.500000:  # try_utf16le
                                return False  # text (100.0%, n=1)
                            else:
                                return True  # binary (100.0%, n=1)
                else:
                    if features[10] <= 0.500000:  # bom_utf16le
                        if features[2] <= 0.456331:  # printable_ascii_ratio
                            if features[5] <= 0.494214:  # even_null_ratio
                                if features[17] <= 0.004608:  # longest_printable_run
                                    return False  # text (100.0%, n=1)
                                else:
                                    if features[6] <= 0.601037:  # odd_null_ratio
                                        if features[7] <= 4.312897:  # byte_entropy
                                            if features[17] <= 0.057190:  # longest_printable_run
                                                return False  # text (66.7%, n=1)
                                            else:
                                                return True  # binary (98.6%, n=1)
                                        else:
                                            return True  # binary (100.0%, n=1)
                                    else:
                                        return False  # text (100.0%, n=1)
                            else:
                                return False  # text (100.0%, n=1)
                        else:
                            if features[17] <= 0.082207:  # longest_printable_run
                                if features[6] <= 0.017636:  # odd_null_ratio
                                    if features[7] <= 6.021909:  # byte_entropy
                                        return False  # text (100.0%, n=1)
                                    else:
                                        return True  # binary (100.0%, n=1)
                                else:
                                    return True  # binary (100.0%, n=1)
                            else:
                                if features[7] <= 4.421185:  # byte_entropy
                                    if features[17] <= 0.138095:  # longest_printable_run
                                        if features[7] <= 4.127879:  # byte_entropy
                                            if features[3] <= 0.446023:  # high_byte_ratio
                                                return True  # binary (100.0%, n=1)
                                            else:
                                                return False  # text (100.0%, n=1)
                                        else:
                                            if features[3] <= 0.459064:  # high_byte_ratio
                                                return False  # text (100.0%, n=1)
                                            else:
                                                return True  # binary (100.0%, n=1)
                                    else:
                                        if features[2] <= 0.645833:  # printable_ascii_ratio
                                            if features[1] <= 0.064583:  # control_ratio
                                                return True  # binary (66.7%, n=1)
                                            else:
                                                return True  # binary (94.7%, n=1)
                                        else:
                                            return False  # text (100.0%, n=1)
                                else:
                                    return True  # binary (100.0%, n=1)
                    else:
                        return False  # text (100.0%, n=1)
        else:
            if features[1] <= 0.177812:  # control_ratio
                if features[0] <= 0.044764:  # null_ratio
                    return False  # text (100.0%, n=1)
                else:
                    return True  # binary (100.0%, n=1)
            else:
                return True  # binary (100.0%, n=1)
