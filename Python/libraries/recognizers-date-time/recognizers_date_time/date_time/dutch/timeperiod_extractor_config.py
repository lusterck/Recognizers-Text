#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List, Pattern

from recognizers_text.utilities import RegExpUtility
from recognizers_text.extractor import Extractor
from recognizers_number.number.dutch.extractors import DutchIntegerExtractor
from ...resources.dutch_date_time import DutchDateTime
from ..extractors import DateTimeExtractor
from ..base_timeperiod import TimePeriodExtractorConfiguration, MatchedIndex
from ..base_time import BaseTimeExtractor
from ..base_timezone import BaseTimeZoneExtractor
from .time_extractor_config import DutchTimeExtractorConfiguration
from .timezone_extractor_config import DutchTimeZoneExtractorConfiguration
from ..utilities import DateTimeOptions


class DutchTimePeriodExtractorConfiguration(TimePeriodExtractorConfiguration):

    @property
    def check_both_before_after(self) -> bool:
        return self._check_both_before_after

    @property
    def dmy_date_format(self) -> bool:
        return self._dmy_date_format

    @property
    def simple_cases_regex(self) -> List[Pattern]:
        return self._simple_cases_regex

    @property
    def till_regex(self) -> Pattern:
        return self._till_regex



    @property
    def time_of_day_regex(self) -> Pattern:
        return self._time_of_day_regex

    @property
    def general_ending_regex(self) -> Pattern:
        return self._general_ending_regex

    @property
    def single_time_extractor(self) -> DateTimeExtractor:
        return self._single_time_extractor

    @property
    def time_zone_extractor(self) -> DateTimeExtractor:
        return self._time_zone_extractor

    @property
    def integer_extractor(self) -> Extractor:
        return self._integer_extractor

    @property
    def token_before_date(self) -> str:
        return self._token_before_date

    @property
    def pure_number_regex(self) -> List[Pattern]:
        return self._pure_number_regex

    @property
    def hour_regex(self) -> Pattern:
        return self._hour_regex

    @property
    def period_hour_num_regex(self) -> Pattern:
        return self._period_hour_num_regex

    @property
    def period_desc_regex(self) -> Pattern:
        return self._period_desc_regex

    @property
    def pm_regex(self) -> Pattern:
        return self._pm_regex

    @property
    def am_regex(self) -> Pattern:
        return self._am_regex

    @property
    def preposition_regex(self) -> Pattern:
        return self._preposition_regex

    @property
    def specific_time_of_day_regex(self) -> Pattern:
        return self._specific_time_of_day_regex

    @property
    def time_unit_regex(self) -> Pattern:
        return self._time_unit_regex

    @property
    def time_followed_unit(self) -> Pattern:
        return self._time_followed_unit

    @property
    def time_number_combined_with_unit(self):
        return self._time_number_combined_with_unit

    @property
    def from_regex(self) -> Pattern:
        return self._from_regex

    @property
    def between_token_regex(self) -> Pattern:
        return self._between_token_regex

    @property
    def range_connector_regex(self) -> Pattern:
        return self._range_connector_regex

    def __init__(self):
        super().__init__()
        self._check_both_before_after = DutchDateTime.CheckBothBeforeAfter
        self._simple_cases_regex: List[Pattern] = [
            RegExpUtility.get_safe_reg_exp(DutchDateTime.PureNumFromTo),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.PureNumBetweenAnd),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.SpecificTimeFromTo),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.SpecificTimeBetweenAnd)
        ]
        self._till_regex: Pattern = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.TillRegex)
        self._time_of_day_regex: Pattern = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.TimeOfDayRegex)
        self._general_ending_regex: Pattern = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.GeneralEndingRegex)
        self._single_time_extractor = BaseTimeExtractor(
            DutchTimeExtractorConfiguration())
        self._integer_extractor = DutchIntegerExtractor()
        self._time_zone_extractor = BaseTimeZoneExtractor(
            DutchTimeZoneExtractorConfiguration())
        self._token_before_date = DutchDateTime.TokenBeforeDate
        self._pure_number_regex = [DutchDateTime.PureNumFromTo, DutchDateTime.PureNumFromTo]
        self._options = DateTimeOptions.NONE
        self._range_connector_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.RangeConnectorRegex)
        self._from_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.FromRegex)
        self._between_token_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.BetweenTokenRegex
        )
        self._preposition_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.PrepositionRegex)

    def get_from_token_index(self, source: str) -> MatchedIndex:
        return MatchedIndex(True, self.from_regex.search(source).start()) if self.from_regex.search(source) else MatchedIndex(False, -1)

    def get_between_token_index(self, source: str) -> MatchedIndex:
        return MatchedIndex(True, self.between_token_regex.search(source).start()) if self.between_token_regex.search(source) else MatchedIndex(False, -1)

    def is_connector_token(self, source: str) -> bool:
        match = self.range_connector_regex.search(source)
        return len(match.group()) == len(source) if match else None
