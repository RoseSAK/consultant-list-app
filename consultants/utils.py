from django.db.models import Q

from consultants.models import Consultant


def search_consultants(search_query):
    query = search_query.lower()
    results = Consultant.objects.filter(Q(consultant_name__icontains=query)  # OR lookup
                                        | Q(contact_number__icontains=query)
                                        | Q(practice__icontains=query)
                                        | Q(role__icontains=query)
                                        | Q(teams__icontains=query)
                                        | Q(skills__icontains=query)
                                        | Q(sectors__icontains=query)
                                        | Q(notes__icontains=query))
    return results

def normalise(text_string):
    normalised_string = text_string.lower()
    return normalised_string