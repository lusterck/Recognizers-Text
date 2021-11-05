#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List, Dict, Callable
import re
from datetime import datetime

from recognizers_text.utilities import RegExpUtility
from ..utilities import DateUtils
from ..base_holiday import BaseHolidayParserConfiguration
from ...resources.dutch_date_time import DutchDateTime


class DutchHolidayParserConfiguration(BaseHolidayParserConfiguration):
    @property
    def holiday_names(self) -> Dict[str, List[str]]:
        return self._holiday_names

    @property
    def holiday_regex_list(self) -> List[str]:
        return self._holiday_regexes

    @property
    def holiday_func_dictionary(self) -> Dict[str, Callable[[int], datetime]]:
        return self._holiday_func_dictionary

    def get_swift_year(self, text: str) -> int:
        trimmed_text = text.strip().lower()
        swift = -10
        if trimmed_text.startswith('volgende'):
            swift = 1
        if trimmed_text.startswith('voorbije'):
            swift = -1
        if trimmed_text.startswith('deze'):
            swift = 0
        return swift

    def sanitize_holiday_token(self, holiday: str) -> str:
        return re.sub('[ \']', '', holiday)

    def __init__(self, config):
        super().__init__()
        self._holiday_regexes = [
            RegExpUtility.get_safe_reg_exp(DutchDateTime.HolidayRegex)
        ]
        self._holiday_names = DutchDateTime.HolidayNames

    def _init_holiday_funcs(self) -> Dict[str, Callable[[int], datetime]]:
        local = dict([
            ('kingsday', DutchHolidayParserConfiguration.kingsday),
            ('queensday', DutchHolidayParserConfiguration.queensday),
            ('prinsjesdag', DutchHolidayParserConfiguration.prinsjesdag),
            ('dodenherdenking', DutchHolidayParserConfiguration.dodenherdenking),
            ('bevrijdingsdag', DutchHolidayParserConfiguration.bevrijdingsdag),
            ('sinterklaas', DutchHolidayParserConfiguration.sinterklaas),
            ('eerstekerstdag', DutchHolidayParserConfiguration.eerstekerstdag),
            ('tweedekerstdag', DutchHolidayParserConfiguration.tweedekerstdag),
            ('dagvandearbeid', DutchHolidayParserConfiguration.dagvandearbeid),
            ('stmartinsday', DutchHolidayParserConfiguration.stmartinsday),
            ('ketikoti', DutchHolidayParserConfiguration.ketikoti),
            ('driekoningen', DutchHolidayParserConfiguration.driekoningen),
            ('fathers', DutchHolidayParserConfiguration.fathers),
            ('goodfriday', DutchHolidayParserConfiguration.goodfriday),
            ('mothers', DutchHolidayParserConfiguration.mothers),
            ('chinesenewyear', DutchHolidayParserConfiguration.chinesenewyear),
            ('maosbirthday', DutchHolidayParserConfiguration.mao_birthday),
            ('yuandan', DutchHolidayParserConfiguration.new_year),
            ('teachersday', DutchHolidayParserConfiguration.teacher_day),
            ('singleday', DutchHolidayParserConfiguration.singles_day),
            ('allsaintsday', DutchHolidayParserConfiguration.halloween_day),
            ('youthday', DutchHolidayParserConfiguration.youth_day),
            ('childrenday', DutchHolidayParserConfiguration.children_day),
            ('femaleday', DutchHolidayParserConfiguration.female_day),
            ('treeplantingday', DutchHolidayParserConfiguration.tree_plant_day),
            ('arborday', DutchHolidayParserConfiguration.tree_plant_day),
            ('girlsday', DutchHolidayParserConfiguration.girls_day),
            ('whiteloverday', DutchHolidayParserConfiguration.white_lover_day),
            ('loverday', DutchHolidayParserConfiguration.valentines_day),
            ('christmas', DutchHolidayParserConfiguration.christmas_day),
            ('xmas', DutchHolidayParserConfiguration.christmas_day),
            ('newyear', DutchHolidayParserConfiguration.new_year),
            ('newyearday', DutchHolidayParserConfiguration.new_year),
            ('newyearsday', DutchHolidayParserConfiguration.new_year),
            ('inaugurationday', DutchHolidayParserConfiguration.inauguration_day),
            ('groundhougday', DutchHolidayParserConfiguration.groundhog_day),
            ('valentinesday', DutchHolidayParserConfiguration.valentines_day),
            ('stpatrickday', DutchHolidayParserConfiguration.st_patrick_day),
            ('aprilfools', DutchHolidayParserConfiguration.fool_day),
            ('stgeorgeday', DutchHolidayParserConfiguration.st_george_day),
            ('mayday', DutchHolidayParserConfiguration.may_day),
            ('cincodemayoday', DutchHolidayParserConfiguration.cinco_de_mayo_day),
            ('baptisteday', DutchHolidayParserConfiguration.baptiste_day),
            ('usindependenceday', DutchHolidayParserConfiguration.usa_independence_day),
            ('independenceday', DutchHolidayParserConfiguration.usa_independence_day),
            ('bastilleday', DutchHolidayParserConfiguration.bastille_day),
            ('halloweenday', DutchHolidayParserConfiguration.halloween_day),
            ('allhallowday', DutchHolidayParserConfiguration.all_hallow_day),
            ('allsoulsday', DutchHolidayParserConfiguration.all_souls_day),
            ('guyfawkesday', DutchHolidayParserConfiguration.guy_fawkes_day),
            ('veteransday', DutchHolidayParserConfiguration.veterans_day),
            ('christmaseve', DutchHolidayParserConfiguration.christmas_eve),
            ('newyeareve', DutchHolidayParserConfiguration.new_year_eve),
            ('easterday', DutchHolidayParserConfiguration.easter_day),
            ('juneteenth', DutchHolidayParserConfiguration.juneteenth),
        ])

        return {**super()._init_holiday_funcs(), **local}

    @staticmethod
    def kingsday(year: int) -> datetime:
        return datetime(year, 4, 27)

    @staticmethod
    def queensday(year: int) -> datetime:
        return datetime(year, 4, 27)

    @staticmethod
    def prinsjesdag(year: int) -> datetime:
        return datetime(year, 9, 20)

    @staticmethod
    def dodenherdenking(year: int) -> datetime:
        return datetime(year, 5, 4)

    @staticmethod
    def bevrijdingsdag(year: int) -> datetime:
        return datetime(year, 5, 5)

    @staticmethod
    def eerstekerstdag(year: int) -> datetime:
        return datetime(year, 12, 25)

    @staticmethod
    def tweedekerstdag(year: int) -> datetime:
        return datetime(year, 12, 26)

    @staticmethod
    def dagvandearbeid(year: int) -> datetime:
        return datetime(year, 5, 1)

    @staticmethod
    def stmartinsday(year: int) -> datetime:
        return datetime(year, 11, 11)

    @staticmethod
    def ketikoti(year: int) -> datetime:
        return datetime(year, 7, 1)

    @staticmethod
    def sinterklaas(year: int) -> datetime:
        return datetime(year, 12, 6)

    @staticmethod
    def driekoningen(year: int) -> datetime:
        return datetime(year, 1, 6)

    @staticmethod
    def fathers(year: int) -> datetime:
        return datetime(year, 1, 20)

    @staticmethod
    def goodfriday(year: int) -> datetime:
        return datetime(year, 4, 15)

    @staticmethod
    def mothers(year: int) -> datetime:
        return datetime(year, 5, 8)

    @staticmethod
    def chinesenewyear(year: int) -> datetime:
        return datetime(year, 2, 1)

    @staticmethod
    def mao_birthday(year: int) -> datetime:
        return datetime(year, 12, 26)

    @staticmethod
    def new_year(year: int) -> datetime:
        return datetime(year, 1, 1)

    @staticmethod
    def teacher_day(year: int) -> datetime:
        return datetime(year, 9, 10)

    @staticmethod
    def singles_day(year: int) -> datetime:
        return datetime(year, 11, 11)

    @staticmethod
    def halloween_day(year: int) -> datetime:
        return datetime(year, 10, 31)

    @staticmethod
    def youth_day(year: int) -> datetime:
        return datetime(year, 5, 4)

    @staticmethod
    def children_day(year: int) -> datetime:
        return datetime(year, 6, 1)

    @staticmethod
    def female_day(year: int) -> datetime:
        return datetime(year, 3, 8)

    @staticmethod
    def tree_plant_day(year: int) -> datetime:
        return datetime(year, 3, 12)

    @staticmethod
    def girls_day(year: int) -> datetime:
        return datetime(year, 3, 7)

    @staticmethod
    def white_lover_day(year: int) -> datetime:
        return datetime(year, 3, 14)

    @staticmethod
    def valentines_day(year: int) -> datetime:
        return datetime(year, 2, 14)

    @staticmethod
    def christmas_day(year: int) -> datetime:
        return datetime(year, 12, 25)

    @staticmethod
    def inauguration_day(year: int) -> datetime:
        return datetime(year, 1, 20)

    @staticmethod
    def groundhog_day(year: int) -> datetime:
        return datetime(year, 2, 2)

    @staticmethod
    def st_patrick_day(year: int) -> datetime:
        return datetime(year, 3, 17)

    @staticmethod
    def fool_day(year: int) -> datetime:
        return datetime(year, 4, 1)

    @staticmethod
    def st_george_day(year: int) -> datetime:
        return datetime(year, 4, 23)

    @staticmethod
    def may_day(year: int) -> datetime:
        return datetime(year, 5, 1)

    @staticmethod
    def cinco_de_mayo_day(year: int) -> datetime:
        return datetime(year, 5, 5)

    @staticmethod
    def baptiste_day(year: int) -> datetime:
        return datetime(year, 6, 24)

    @staticmethod
    def usa_independence_day(year: int) -> datetime:
        return datetime(year, 7, 4)

    @staticmethod
    def bastille_day(year: int) -> datetime:
        return datetime(year, 7, 14)

    @staticmethod
    def all_hallow_day(year: int) -> datetime:
        return datetime(year, 11, 1)

    @staticmethod
    def all_souls_day(year: int) -> datetime:
        return datetime(year, 11, 2)

    @staticmethod
    def guy_fawkes_day(year: int) -> datetime:
        return datetime(year, 11, 5)

    @staticmethod
    def veterans_day(year: int) -> datetime:
        return datetime(year, 11, 11)

    @staticmethod
    def christmas_eve(year: int) -> datetime:
        return datetime(year, 12, 24)

    @staticmethod
    def new_year_eve(year: int) -> datetime:
        return datetime(year, 12, 31)

    @staticmethod
    def easter_day(year: int) -> datetime:
        return DateUtils.min_value

    @staticmethod
    def juneteenth(year: int) -> datetime:
        return datetime(year, 6, 19)
