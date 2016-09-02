# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase, CMSPlugin
import models
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _


class MBDAboutTeamBarPlugin(CMSPluginBase):
    """
    DJANGO CMS Plugin to display a team bar
    """
    model = models.MBDAboutTeamBar
    name = _("MBD Team Bar")
    render_template = "mbd_template/plugins/teambar.html"
    cache = False
    module = "MBD"


class MBDAboutBoardMemberSocialIconsPlugin(CMSPluginBase):
    """
    Display the needed social icons inside MBDAboutBoardMemberCardPlugin plugin
    """
    model = models.MBDAboutBoardMemberSocialIcons
    name = _("MBD Board Member Social Icons")
    render_template = "mbd_template/plugins/memsocialicons.html"
    cache = True
    require_parent = True
    parent_classes = ['MBDAboutBoardMemberCardPlugin']
    allow_children = False


class MBDAboutBoardMemberCardPlugin(CMSPluginBase):
    """
    DJANGO CMS Plugin to display a team bar
    """
    model = models.MBDBoardMemberCard
    name = _("MBD Board Member Card")
    render_template = "mbd_template/plugins/memcard.html"
    cache = True
    allow_children = True
    child_classes = ['MBDAboutBoardMemberSocialIconsPlugin']
    module = "MBD"

class MBDDancerBadge(CMSPluginBase):
    """
    DJANGO CMS Plugin to display the picture and a small caption about a dancer
    """
    model = models.MBDDancerBadge
    name = _("MBD Dancer Badge")
    render_template = "mbd_template/plugins/dancerbadge.html"
    cache = True
    module = "MBD"
    allow_children = False

plugin_pool.register_plugin(MBDAboutTeamBarPlugin)
plugin_pool.register_plugin(MBDAboutBoardMemberCardPlugin)
plugin_pool.register_plugin(MBDAboutBoardMemberSocialIconsPlugin)
plugin_pool.register_plugin(MBDDancerBadge)