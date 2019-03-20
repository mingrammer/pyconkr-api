import graphene
from graphene_django import DjangoObjectType
from graphql_extensions.auth.decorators import login_required

from api.models.sponsor import Sponsor, SponsorLevel
from api.schemas.common import SeoulDateTime
from api.schemas.user import UserNode


class SponsorNode(DjangoObjectType):
    class Meta:
        model = Sponsor
        description = """
        Sponsors which spon python conference in Korea.
        """

    paid_at = graphene.Field(SeoulDateTime)


class SponsorLevelNode(DjangoObjectType):
    class Meta:
        model = SponsorLevel
        description = """
        The level of sponsors, python conference in Korea.
        """

class SponsorInput(graphene.InputObjectType):
    name = graphene.String()
    name_ko = graphene.String()
    name_en = graphene.String()
    desc = graphene.String()
    desc_ko = graphene.String()
    desc_en = graphene.String()
    url = graphene.String()
    level = graphene.Field(SponsorLevelNode)
    paidAt = graphene.Date()


class CreateOrUpdateSponsor(graphene.Mutation):
    sponsor = graphene.Field(SponsorNode)

    class Arguments:
        sponsor_input = SponsorInput(required=True)

    @login_required
    def mutate(self, info, sponsor_input):
        user = info.context.user

        if hasattr(user, 'sponsor'):
            sponsor = user.sponsor
        else:
            sponsor = Sponsor()
            sponsor.owner = user


        for k, v in sponsor_input.items():
            setattr(sponsor, k, v)

        sponsor.full_clean()
        sponsor.save()
        return CreateOrUpdateSponsor(sponsor=sponsor)



class Mutations(graphene.ObjectType):
    create_or_update_presentation = CreateOrUpdateSponsor.Field()



class Query(graphene.ObjectType):
    ticketUsers = graphene.List(UserNode)
    sponsorLevel = graphene.Field(SponsorLevelNode)

    sponsor = graphene.Field(SponsorNode)
    sponsors = graphene.List(SponsorNode)

    def resolve_sponsors(self, info):
        return Sponsor.objects.all()
