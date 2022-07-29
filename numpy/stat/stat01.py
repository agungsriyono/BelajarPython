import numpy
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

rata = numpy.mean(speed)
median = numpy.median(speed)
modus = stats.mode(speed)
std = numpy.std(speed)
variance = numpy.var(speed)
p95 = numpy.percentile(speed,95)



print(f'Rata-ratanya : {rata}')
print(f'Median-nya : {median}')
print(f'Modus-nya : {modus}')
print(f'standard deviasi-nya : {std}')
print(f'Variance-nya : {variance}')
print(f'Percentile 95-nya : {p95}')

