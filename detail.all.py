#!/usr/bin/env python3
#
#

from fundamentus import get_detalhes_list
from fundamentus import print_csv
from fundamentus.papel import get_list_papel

from datetime import datetime, timedelta


if __name__ == '__main__':

    my_list = get_list_papel()

#   df = get_detalhes_list(my_list[80:110])
    df = get_detalhes_list(my_list)

    df.index.name = 'papel'

    # skip older companies
    dsince = datetime.today() - timedelta(days=10)
    _since = dsince.strftime('%Y-%m-%d')

    result = df[ df['Data_ult_cot'] > _since ]

    # today's csv
    fname = 'bovespa.detalhes.{}.csv'.format(_today)
    result.to_csv(fname)

