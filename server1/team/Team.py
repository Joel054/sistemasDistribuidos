
from .models import Member, Team
from django.shortcuts import render

# request padrão


def return_team(request, context):
    user = request.user
    members = Member.objects.filter(id_user=user.id)
    memb = []
    for member in members:
        try:
            team = Team.objects.get(id=member.id_team)
            memb.append({'name': team.name, 'description': team.description, 'status': team.status, 'id': team.id})

        except Team.DoesNotExist:
            a = 1
    append = {'members': memb}
    if context is not None:
        context.update(append)
    else:
        context = append
    return render(request, 'teams.html', context)



