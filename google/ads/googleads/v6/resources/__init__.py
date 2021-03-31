# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


__all__ = (
    "AccountBudgetProposal",
    "AccountLink",
    "Ad",
    "AdGroup",
    "AdGroupAd",
    "AdGroupAdAssetPolicySummary",
    "AdGroupAdAssetView",
    "AdGroupAdLabel",
    "AdGroupAdPolicySummary",
    "AdGroupAudienceView",
    "AdGroupBidModifier",
    "AdGroupCriterion",
    "AdGroupCriterionLabel",
    "AdGroupCriterionSimulation",
    "AdGroupExtensionSetting",
    "AdGroupFeed",
    "AdGroupLabel",
    "AdGroupSimulation",
    "AdParameter",
    "AdScheduleView",
    "AgeRangeView",
    "Asset",
    "AssetPolicySummary",
    "AttributeFieldMapping",
    "BatchJob",
    "BiddingStrategy",
    "BillingSetup",
    "CallReportingSetting",
    "CallView",
    "Campaign",
    "CampaignAsset",
    "CampaignAudienceView",
    "CampaignBidModifier",
    "CampaignBudget",
    "CampaignCriterion",
    "CampaignCriterionSimulation",
    "CampaignDraft",
    "CampaignExperiment",
    "CampaignExtensionSetting",
    "CampaignFeed",
    "CampaignLabel",
    "CampaignSharedSet",
    "CarrierConstant",
    "ChangeEvent",
    "ChangeStatus",
    "ClickView",
    "CombinedAudience",
    "ConversionAction",
    "ConversionTrackingSetting",
    "CurrencyConstant",
    "CustomAudience",
    "CustomAudienceMember",
    "CustomInterest",
    "CustomInterestMember",
    "Customer",
    "CustomerClient",
    "CustomerClientLink",
    "CustomerExtensionSetting",
    "CustomerFeed",
    "CustomerLabel",
    "CustomerManagerLink",
    "CustomerNegativeCriterion",
    "CustomerUserAccess",
    "CustomerUserAccessInvitation",
    "DataPartnerLinkIdentifier",
    "DetailPlacementView",
    "DisplayKeywordView",
    "DistanceView",
    "DomainCategory",
    "DynamicSearchAdsSearchTermView",
    "ExpandedLandingPageView",
    "ExtensionFeedItem",
    "Feed",
    "FeedAttribute",
    "FeedAttributeOperation",
    "FeedItem",
    "FeedItemAttributeValue",
    "FeedItemPlaceholderPolicyInfo",
    "FeedItemSet",
    "FeedItemSetLink",
    "FeedItemTarget",
    "FeedItemValidationError",
    "FeedMapping",
    "FeedPlaceholderView",
    "GenderView",
    "GeoTargetConstant",
    "GeographicView",
    "GoogleAdsField",
    "GoogleAdsLinkIdentifier",
    "GroupPlacementView",
    "HotelGroupView",
    "HotelPerformanceView",
    "IncomeRangeView",
    "Invoice",
    "KeywordPlan",
    "KeywordPlanAdGroup",
    "KeywordPlanAdGroupKeyword",
    "KeywordPlanCampaign",
    "KeywordPlanCampaignKeyword",
    "KeywordPlanForecastPeriod",
    "KeywordPlanGeoTarget",
    "KeywordView",
    "Label",
    "LandingPageView",
    "LanguageConstant",
    "LocationView",
    "ManagedPlacementView",
    "MediaAudio",
    "MediaBundle",
    "MediaFile",
    "MediaImage",
    "MediaVideo",
    "MerchantCenterLink",
    "MobileAppCategoryConstant",
    "MobileDeviceConstant",
    "OfflineUserDataJob",
    "OperatingSystemVersionConstant",
    "PaidOrganicSearchTermView",
    "ParentalStatusView",
    "PaymentsAccount",
    "ProductBiddingCategoryConstant",
    "ProductGroupView",
    "Recommendation",
    "RemarketingAction",
    "RemarketingSetting",
    "SearchTermView",
    "SharedCriterion",
    "SharedSet",
    "ShoppingPerformanceView",
    "ThirdPartyAppAnalyticsLink",
    "ThirdPartyAppAnalyticsLinkIdentifier",
    "TopicConstant",
    "TopicView",
    "UserInterest",
    "UserList",
    "UserLocationView",
    "Video",
    "AccountBudget",
)
