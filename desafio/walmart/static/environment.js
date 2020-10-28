var moduleExport = false
if (typeof window === 'undefined' ) {
    var window = {}
    moduleExport = true
}

window.__ENV__ = {
    appId: "529CV9H7MW",
    apiKey: "c6ab9bc3e19c260e6bad42abe143d5f4",
    indexName: "campaigns_production_search",
    storageBaseUrl: "https://buysmartstatic.lider.cl/landing",
    ssttJsonPath: "json/sstt.json?ts="+new Date().getTime(),
    supermarketItemsJsonPath: "json/supermarketItems.json?ts="+new Date().getTime(),
    bannersJsonPath: "json/banners.json?ts="+new Date().getTime(),
    bannersPath: "banners",
    homeCampaignIdFilter: "blackcyber",
    ridiculouslyLowPrice: "json/ridiculouslyLowPrice.json",
    countDownBanner: "json/countDownBanner.json",
    campaignConfig: "json/campaignConfig.json",
    categoryPageConfig: "json/categoryPageConfig.json",
    homePageConfig: "json/homePageConfig.json",
    productPageConfig: "json/productPageConfig.json",
    searchWithoutResultToCategory: "json/searchWithoutResultToCategory.json",
    liderGrocery: "https://www.lider.cl/supermercado",
    baseURL: "https://buysmart-landing-bff-production.lider.cl/buysmart-checkout-bff/",
    timeout: 60000,
    ssrEnabled: true,
    keyHotjar: "1599898",
    baseURLbff: "https://buysmart-bff-production.lider.cl/buysmart-bff/",
    newBff: true,
    logger: true,
    siteToStoreValueAmount: 19990,
    imagesPath: "images",
    isWalstore: "",
    tagManagerId: "GTM-TZWFDQM"
}

if (moduleExport) {
    module.exports = window
}
