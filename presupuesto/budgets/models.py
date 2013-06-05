from django.db import models


class Category(models.Model):
    description = models.CharField(max_length=100)
    default_amount = models.FloatField()

    def get_amount_for_month(self, month_number):
        try:
            specific_amount = self.specific_amounts.get(
                month_number=month_number,
                )
        except SpecificMonthAmount.DoesNotExist:
            amount = self.default_amount
        else:
            amount = specific_amount.amount

        return amount

    def get_amounts_by_month(self):
        amounts_by_month = []
        for month_number in range(1, 13):
            amounts_by_month.append(self.get_amount_for_month(month_number))
        return amounts_by_month

    def __str__(self):
        return self.description


class SpecificMonthAmount(models.Model):
    category = models.ForeignKey(Category, related_name="specific_amounts")
    month_number = models.PositiveSmallIntegerField()
    amount = models.FloatField()

    class Meta:
        unique_together = (("category", "month_number"),)

    def __str__(self):
        return "Budget for %s in month #%s" % (self.category, self.month_number)
