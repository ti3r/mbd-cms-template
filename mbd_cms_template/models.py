from django.db import models
import cms
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField


class MBDAboutTeamBar(CMSPlugin):
    """
    Plugin to describe the information stored for a Team Bar in the Template
    """
    sections = models.PositiveSmallIntegerField(default=4, null=False, blank=False,
                                                verbose_name=_("Number of sections the bar will be divided"),
                                                help_text=_(
                                                    "Describe the number of sections the bar will be divided showing arrows "
                                                    "up and down for each section"))

    def get_range(self):
        return range(self.sections)

    def get_width(self):
        return (80 / self.sections)


class MBDBoardMemberCard(CMSPlugin):
    """
    Plugin to show a board member presentation card. This plugin is mainly used in the
    about page
    """
    name = models.CharField(null=False, blank=False, help_text=_("Main name to display on the card"),
                            verbose_name=_("Name"), max_length=60)
    title = models.CharField(null=False, blank=False, help_text=_("Title of the board member"), verbose_name=_("Title"),
                             max_length=60)
    bio = models.TextField(null=False, blank=False, help_text=_("Brief biography of the member"), verbose_name=_("Bio"))
    picture = FilerImageField(null=True, blank=True, default=None, verbose_name=_("image"), on_delete=models.SET_NULL,
                              help_text=_("Member Picture"))
    point_up = models.BooleanField(null=False, blank=False, default=False, verbose_name=_("Point Card Up"),
                                   help_text=_("Display the indicator of the card pointing up. "
                                               "Designed for cards that will show below the team line"))
    offset = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_("Bootstrap Column Offset"),
                                              help_text=_("The offset in bootstrap column the card should appear at."
                                                          "See column offset in bootstrap"))


class MBDAboutBoardMemberSocialIcons(CMSPlugin):
    """
    Plugin model to specify the social icons that will be displayed in a MBDBoardMemberCardPlugin plugin
    """
    facebook = models.URLField(null=True, blank=True, help_text=_("Url to the facebook profile page"),
                               verbose_name=_("Facebook Url"))
    twitter = models.URLField(null=True, blank=True, help_text=_("Url to the twitter profile page"),
                              verbose_name=_("Twitter Url"))
    google_plus = models.URLField(null=True, blank=True, help_text=_("Url to the google plus profile page"),
                                  verbose_name=_("Google+ Url"))
    instagram = models.URLField(null=True, blank=True, help_text=_("Url to the instagram profile page"),
                                verbose_name=_("Instagram Url"))
    youtube = models.URLField(null=True, blank=True, help_text=_("Url to the yourube channel page"),
                              verbose_name=_("Youtube Url"))
    pinterest = models.URLField(null=True, blank=True, help_text=_("Url to the pinterest profile page"),
                                verbose_name=_("Pinterest Url"))


class MBDDancerBadge(CMSPlugin):
    """
    Plugin model to store the configuration of the badge display
    """
    picture = FilerImageField(null=True, blank=True, default=None, verbose_name=_("picture"), on_delete=models.SET_NULL,
                              help_text=_("Dancer Picture"))
    name = models.CharField(null=False, blank=False, help_text=_("Main name to display on the badge"),
                            verbose_name=_("Name"), max_length=60)
    alt_text = models.CharField(null=False, blank=False, help_text=_("Text to display after the name"),
                                verbose_name=_("Alternate Text"), max_length=60)


class MBDancerPicture(CMSPlugin):
    """
    Plugin model to store the configuration for the dancer picture plugin
    """
    picture = FilerImageField(null=True, blank=True, default=None, verbose_name=_("picture"), on_delete=models.SET_NULL,
                              help_text=_("Dancer Picture"))
    name = models.CharField(null=False, blank=False, help_text=_("Main name to display on the badge"),
                            verbose_name=_("Name"), max_length=60)
    small_bio = models.CharField(null=False, blank=False, help_text=_("Small text that will appear when hover"),
                                 verbose_name=_("Small Bio"), max_length=60)
    link_page = cms.models.fields.PageField(verbose_name=_("Link"), blank=False, null=True,
                                            help_text=_("Url to visit when read more is selected"))


class MBDTwoPicCarousel(CMSPlugin):
    """
    Plugin in model to store information for the MBDTwoPicCarouselPlugin
    """
    slide1_background = FilerImageField(null=True, blank=True, default=None, verbose_name=_("Slide 1 Main Picture"),
                                        on_delete=models.SET_NULL, related_name="slide1_background",
                                        help_text=_("Picture for slide 1 background"))
    slide1_foreground = FilerImageField(null=True, blank=True, default=None,
                                        verbose_name=_("Slide 1 Foreground Picture"),
                                        on_delete=models.SET_NULL, related_name="slide1_foreground",
                                        help_text=_("Picture for slide 1 foreground"))
    slide1_header = models.CharField(null=True, blank=True, help_text=_("Header text that will appear in slide 1"),
                                     verbose_name=_("Slide 1 Header"), max_length=60)
    slide1_caption = models.CharField(null=True, blank=True,
                                      help_text=_("Caption text that will appear in slide 1 below header"),
                                      verbose_name=_("Slide 1 Header"), max_length=120)
    slide1_button_text = models.CharField(null=True, blank=True,
                                          help_text=_(
                                              "Text to show in a button below the caption of the slide if wanted"),
                                          verbose_name=_("Slide 1 Button Text"), max_length=25)
    slide1_button_link = cms.models.fields.PageField(null=True, blank=True, related_name="slide1_button_link",
                                                     help_text=_("Page to visit once the button is clicked"),
                                                     verbose_name=_("Slide 1 Button Link"))
    slide2_background = FilerImageField(null=True, blank=True, default=None, verbose_name=_("Slide 2 Main Picture"),
                                        on_delete=models.SET_NULL, related_name="slide2_background",
                                        help_text=_("Picture for slide 2 background"))
    slide2_foreground = FilerImageField(null=True, blank=True, default=None,
                                        verbose_name=_("Slide 2 Foreground Picture"),
                                        on_delete=models.SET_NULL, related_name="slide2_foreground",
                                        help_text=_("Picture for slide 2 foreground"))
    slide2_header = models.CharField(null=True, blank=True, help_text=_("Header text that will appear in slide 2"),
                                     verbose_name=_("Slide 2 Header"), max_length=60)
    slide2_caption = models.CharField(null=True, blank=True,
                                      help_text=_("Caption text that will appear in slide 2 below header"),
                                      verbose_name=_("Slide 2 Header"), max_length=120)
    slide2_button_text = models.CharField(null=True, blank=True,
                                          help_text=_(
                                              "Text to show in a button below the caption of the slide if wanted"),
                                          verbose_name=_("Slide 2 Button Text"), max_length=25)
    slide2_button_link = cms.models.fields.PageField(null=True, blank=True, related_name="slide2_button_link",
                                                     help_text=_("Page to visit once the button is clicked"),
                                                     verbose_name=_("Slide 2 Button Link"))
    slide3_background = FilerImageField(null=True, blank=True, default=None, verbose_name=_("Slide 3 Main Picture"),
                                        on_delete=models.SET_NULL, related_name="slide3_background",
                                        help_text=_("Picture for slide 3 background"))
    slide3_foreground = FilerImageField(null=True, blank=True, default=None,
                                        verbose_name=_("Slide 3 Foreground Picture"),
                                        on_delete=models.SET_NULL, related_name="slide3_foreground",
                                        help_text=_("Picture for slide 3 foreground"))
    slide3_header = models.CharField(null=True, blank=True, help_text=_("Header text that will appear in slide 3"),
                                     verbose_name=_("Slide 3 Header"), max_length=60)
    slide3_caption = models.CharField(null=True, blank=True,
                                      help_text=_("Caption text that will appear in slide 3 below header"),
                                      verbose_name=_("Slide 3 Header"), max_length=120)
    slide3_button_text = models.CharField(null=True, blank=True,
                                          help_text=_(
                                              "Text to show in a button below the caption of the slide if wanted"),
                                          verbose_name=_("Slide 1 Button Text"), max_length=25)
    slide3_button_link = cms.models.fields.PageField(null=True, blank=True, related_name="slide3_button_link",
                                                     help_text=_("Page to visit once the button is clicked"),
                                                     verbose_name=_("Slide 3 Button Link"))
    slide4_background = FilerImageField(null=True, blank=True, default=None, verbose_name=_("Slide 4 Main Picture"),
                                        on_delete=models.SET_NULL, related_name="slide4_background",
                                        help_text=_("Picture for slide 4 background"))
    slide4_foreground = FilerImageField(null=True, default=None, blank=True,
                                        verbose_name=_("Slide 4 Foreground Picture"),
                                        on_delete=models.SET_NULL, related_name="slide4_foreground",
                                        help_text=_("Picture for slide 4 foreground"))
    slide4_header = models.CharField(null=True, blank=True, help_text=_("Header text that will appear in slide 4"),
                                     verbose_name=_("Slide 4 Header"), max_length=60)
    slide4_caption = models.CharField(null=True, blank=True,
                                      help_text=_("Caption text that will appear in slide 4 below header"),
                                      verbose_name=_("Slide 4 Header"), max_length=120)
    slide4_button_text = models.CharField(null=True, blank=True,
                                          help_text=_(
                                              "Text to show in a button below the caption of the slide if wanted"),
                                          verbose_name=_("Slide 4 Button Text"), max_length=25)
    slide4_button_link = cms.models.fields.PageField(null=True, blank=True, related_name="slide4_button_link",
                                                     help_text=_("Page to visit once the button is clicked"),
                                                     verbose_name=_("Slide 4 Button Link"))
