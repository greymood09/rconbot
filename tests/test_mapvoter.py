#! /usr/bin/env python3

# Copyright (C) 2019 Basheer Subei
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.
#
# A testing class to test the MapVoter functionality.
#

import pytest
from unittest import mock

from mapvoter import mapvoter


class TestMapVoter:
    """ TODO docstring """

    @pytest.fixture
    def voter(self):
        """ The fixture function to return a mapvoter. """
        return mapvoter.MapVoter()

    def check_should_start_map_vote(voter, time_map_started, time_now, expected_should_start):
        voter.time_map_started = time_map_started
        with mock.patch('mapvoter.mapvoter.time.time') as mock_time:
            mock_time.return_value = time_now
            assert expected_should_start == voter.should_start_map_vote()

    def test_should_start_map_vote(self, voter):
        """ Tests for should_start_map_vote. """
        # Case 1: On startup, a mapvoter should never want to start a map vote.
        TIME_NOW = 42.0
        TestMapVoter.check_should_start_map_vote(
            voter, TIME_NOW, TIME_NOW, False)

        # Case 2: After not enough time has elapsed, a mapvoter should not want to start a map vote.
        TestMapVoter.check_should_start_map_vote(
            voter, TIME_NOW, TIME_NOW + mapvoter.TIME_ELAPSED_BEFORE_STARTING_VOTE_S - 1.0, False)

        # Case 3: After enough time has elapsed, a mapvoter should want to start a map vote.
        TestMapVoter.check_should_start_map_vote(
            voter, TIME_NOW, TIME_NOW + mapvoter.TIME_ELAPSED_BEFORE_STARTING_VOTE_S + 1.0, True)

    def test_reset_new_map(self, voter):
        """ Tests for reset_new_map. """
        # Time elapsed should reset every time reset_new_map is called.
        initial_time = voter.time_map_started
        voter.reset_new_map()
        later_time = voter.time_map_started
        assert later_time > initial_time
