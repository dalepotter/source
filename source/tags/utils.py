from django.db.models import Q
from django.http import Http404

from .models import TechnologyTag, ConceptTag
from taggit.models import Tag

def filter_queryset_by_tags(queryset, tag_slugs, tags=[]):
    '''
    This takes a queryset and a set of tag slugs, and:
    - does the proper checks to make sure that each tag actually exists
    - filters the provided queryset based on those tags
    - returns that queryset along with a list of matched tag model instances
    for use in page context
    
    Because we need to match against multiple tag models, we have to do
    some loops I wish we didn't have to do. This is why we cache.
    
    The `tag_slugs` argument should be a string captured by a url param,
    with individual tags separated by a "+" character. The `tags` argument
    should very likely be an empty list, which will end up holding a set
    of model instances for the tags from `tag_slugs`.
    '''

    _tag_slug_list = tag_slugs.split('+')
    _slugs_checked = []
    for slug in _tag_slug_list:
        for model in [Tag, TechnologyTag, ConceptTag]:
            try:
                # see if we have a matching tag
                found_tag = model.objects.get(slug=slug)
                # add it to list for page context
                tags.append(found_tag)
                # remember that we've checked it
                _slugs_checked.append(slug)
                break
            except:
                pass

    # make sure that we found everything we checked for
    if _slugs_checked != _tag_slug_list:
        raise Http404
    
    for tag_slug in _tag_slug_list:
        # Look for matches in both types of tagfields
        # TODO: Remove original `tags` query once content migrates
        # to new split tagfields
        queryset = queryset.filter(Q(tags__slug=tag_slug) | Q(technology_tags__slug=tag_slug) | Q(concept_tags__slug=tag_slug))
        # A record might match multiple tags, but we only want it once
        queryset = queryset.distinct()

    # make sure we actually have matches for this intersection of tags
    if not queryset:
        raise Http404
    
    return queryset, tags
