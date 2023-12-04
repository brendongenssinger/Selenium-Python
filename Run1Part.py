from selenium import webdriver
from seleniumPython import downloadVideo,downloadVideoClass


def ExecuteAll(driver):

    #region Acesso ao Abdome
    # downloadVideo(driver,"//*[@id=\"learning-module-title-_9163_1\"]"
    #             ,"//*[@id=\"learning-module-contents-_9163_1\"]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/a"
    #             ,"//*[@id=\"bbml-editor-id_af22dded-b55f-4dfa-8a57-498e321cd5fe-rte\"]/div/div/iframe")


    # downloadVideo(driver,""
    #             ,"//*[@id=\"learning-module-contents-_9163_1\"]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/a"
    #             ,"//*[@id=\"bbml-editor-id_0d202337-04f3-463a-b83a-894d1150aed0-rte\"]/div/div/iframe")
    #endregion

    #region Cirurgias Reconstrutivas

        # downloadVideo(driver,"//*[@id=\"learning-module-title-_2123_1\"]"
        #             ,"//*[@id=\"learning-module-contents-_2123_1\"]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/a"
        #             ,"//*[@id=\"bbml-editor-id_30914d20-70d5-4026-bfd1-71137cfd453d-rte\"]/div/div/iframe")

        # downloadVideo(driver,""
        #             ,"//*[@id=\"learning-module-contents-_2123_1\"]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/a"
        #             ,"//*[@id=\"bbml-editor-id_fd273e96-90aa-480d-83e1-17ab4261f001-rte\"]/div/div/iframe")

        # downloadVideo(driver,""
        #             ,"//*[@id=\"learning-module-contents-_2123_1\"]/div/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/a"
        #             ,"//*[@id=\"bbml-editor-id_35549d44-7eb7-469d-86b1-74d1948c0eeb-rte\"]/div/div/iframe")

        #Retalhos de plexo subdérmico pt 2 + enxertos
        # downloadVideo(driver,""
        #             ,"//*[@id=\"learning-module-contents-_2123_1\"]/div/div[1]/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/a"
        #             ,"//*[@id=\"bbml-editor-id_6d24f468-dc3d-4266-813b-bce1c91c89ff-rte\"]/div/div/iframe")

    #endregion

    #region Praticas- suturas, anatomia e paramentação
    print('Praticas - Suturas, Anatomia e Paramentação')
    
    downloadVideo(driver,"//*[@id=\"learning-module-title-_2033_1\"]"
                ,"//*[@id=\"learning-module-contents-_2033_1\"]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/a"
                ,"//*[@id=\"bbml-editor-id_aa42f3db-4f29-4e84-8a4a-2bf402538140-rte\"]/div/div/iframe")
#Error Here
    downloadVideo(driver,""
                ,"//*[@id=\"learning-module-contents-_2033_1\"]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/a"
                ,"//*[@id=\"bbml-editor-id_e419e66f-ca86-4599-a7e4-3e8904d4fcfb-rte\"]/div/div/iframe")

    # downloadVideo(driver,""
    #             ,"//*[@id=\"learning-module-contents-_2033_1\"]/div/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/a"
    #             ,"//*[@id=\"bbml-editor-id_8263c6e1-ad1d-4cd3-b274-7e9511a4edad-rte\"]/div/div/iframe")


    #region Anatomia tórax
    # downloadVideo(driver,""
    #             ,"//*[@id=\"learning-module-contents-_2033_1\"]/div/div[1]/div[2]/div[5]/div/div/div[2]/div/div[1]/div[1]/a"
    #             ,"//*[@id=\"bbml-editor-id_beb429be-fe9b-46ad-9f21-095cb446a3c7-rte\"]/div/div/iframe")
    #endregion

    #region Anatomia abdome - rim e adrenal
    # downloadVideo(driver,""
    #             ,"//*[@id=\"learning-module-contents-_2033_1\"]/div/div[1]/div[2]/div[6]/div/div/div[2]/div/div[1]/div[1]/a"
    #             ,"//*[@id=\"bbml-editor-id_5175d990-c43c-48e1-a81e-7166a23c8246-rte\"]/div/div/iframe")
    #endregion
    #region Anatomia pescoço
    downloadVideo(driver,""                  
                ,"//*[@id=\"learning-module-contents-_2033_1\"]/div/div[1]/div[2]/div[8]/div/div/div[2]/div/div[1]/div[1]/a"
                ,"//*[@id=\"bbml-editor-id_5409dae7-de84-4360-a163-99df8530dc94-rte\"]/div/div/iframe")
    #endregion
    #region Anatomia face
    # downloadVideo(driver,""
    #             ,"//*[@id=\"learning-module-contents-_2033_1\"]/div/div[1]/div[2]/div[9]/div/div/div[2]/div/div[1]/div[1]/a"
    #             ,"//*[@id=\"bbml-editor-id_5d235a4c-f16a-4d0a-9cd9-3bd6849e19ca-rte\"]/div/div/iframe")
    #endregion
#Error here    


    #region Nó de cirurgião
    # downloadVideo(driver,""
    #             ,"//*[@id=\"learning-module-contents-_2033_1\"]/div/div[1]/div[2]/div[10]/div/div/div[2]/div/div[1]/div[1]/a"
    #             ,"//*[@id=\"bbml-editor-id_35dafc56-6f8b-414e-b061-fb38e2d6b6d6-rte\"]/div/div/iframe")
    #endregion

#Error Here
    #region Orientações do nó
    downloadVideo(driver,""
                ,"//*[@id=\"learning-module-contents-_2033_1\"]/div/div[1]/div[2]/div[11]/div/div/div[2]/div/div[1]/div[1]/a"
                ,"//*[@id=\"bbml-editor-id_fbe503cf-7e58-4dec-86f8-5e56a13a7d68-rte\"]/div/div/iframe")
    #endregion
#Error Here
    #region 4
    downloadVideo(driver,""
                ,f"//*[@id=\"learning-module-contents-_2033_1\"]/div/div[1]/div[2]/div[12]/div/div/div[2]/div/div[1]/div[1]/a"
                ,"//*[@id=\"bbml-editor-id_077b553e-53de-4b6f-ae75-5a2abe67b011-rte\"]/div/div/iframe")
    #endregion
#Error Here
    #region Karatê chop
    downloadVideo(driver,""
                ,"//*[@id=\"learning-module-contents-_2033_1\"]/div/div[1]/div[2]/div[13]/div/div/div[2]/div/div[1]/div[1]/a"
                ,"//*[@id=\"bbml-editor-id_3d8ccc0d-5b7e-4c0d-9958-fbc05bda27ff-rte\"]/div/div/iframe")
    #endregion
    #endregion

    #region Primeiro Modulo 
    # downloadVideo(driver,"//*[@id=\"learning-module-title-_664_1\"]"
    #             ,"//*[@id=\"learning-module-contents-_664_1\"]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/a"
    #             ,"//*[@id=\"bbml-editor-id_cc190fe3-01cd-48a4-b9c6-b157685d0ca4-rte\"]/div/div/iframe")
    #region Princípios cirurgicos
        # downloadVideoClass(driver,
        # "#learning-module-contents-_664_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-253.makeStylescontentList-0-2-347 > div:nth-child(3) > div > div > div.makeStylescontentItemComponent-0-2-267 > div > div.makeStylescontentItemContentArea-0-2-270 > div.makeStylescontainer-0-2-304 > a"
        # ,"#player > div.vp-player-ui-overlays > div.vp-title.Title_module_title__1f69cee0 > header > div.Title_module_headers__1f69cee0 > a.Title_module_subtitleLink__1f69cee0.shared_module_focusable__63d26f6d.Link_module_link__b2eb3a07")
    #endregion


    # downloadVideoClass(driver,""
    #             ,"#learning-module-contents-_664_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-253.makeStylescontentList-0-2-347 > div:nth-child(6) > div > div > div.makeStylescontentItemComponent-0-2-267 > div > div.makeStylescontentItemContentArea-0-2-270 > div.makeStylescontainer-0-2-304 > a"
    #             ,"#bbml-editor-id_471c6310-7253-475b-a758-9d7bbdfc0b09-rte > div > div > iframe")

    # downloadVideoClass(driver,""
    #             ,"#learning-module-contents-_664_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-253.makeStylescontentList-0-2-347 > div:nth-child(8) > div > div > div.makeStylescontentItemComponent-0-2-267 > div > div.makeStylescontentItemContentArea-0-2-270 > div.makeStylescontainer-0-2-304 > a"
    #             ,"#bbml-editor-id_88683a0f-56a5-4723-8d66-20023ff38efa-rte > div > div > iframe")

    # downloadVideoClass(driver,""
    #             ,"#learning-module-contents-_664_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-253.makeStylescontentList-0-2-347 > div:nth-child(9) > div > div > div.makeStylescontentItemComponent-0-2-267 > div > div.makeStylescontentItemContentArea-0-2-270 > div.makeStylescontainer-0-2-304 > a"
    #             ,"#bbml-editor-id_1e2c7a2a-ba8d-4e0e-96ba-1983bb522dff-rte > div > div > iframe")

    #endregion

    #region Manejo e Tratamento de feridas

    # downloadVideoClass(driver,"#learning-module-title-_1754_1"
    #             ,"#learning-module-contents-_1754_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-253.makeStylescontentList-0-2-377 > div:nth-child(1) > div > div > div.makeStylescontentItemComponent-0-2-267 > div > div.makeStylescontentItemContentArea-0-2-270 > div.makeStylescontainer-0-2-304 > a"
    #             ,"#bbml-editor-id_cc8b0c7b-5269-4128-abb9-6c54fa89b07c-rte > div > div > iframe")

    # downloadVideoClass(driver,""
    #             ,"#learning-module-contents-_1754_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-253.makeStylescontentList-0-2-377 > div:nth-child(2) > div > div > div.makeStylescontentItemComponent-0-2-267 > div > div.makeStylescontentItemContentArea-0-2-270 > div.makeStylescontainer-0-2-304 > a"
    #             ,"#bbml-editor-id_ea2926ec-8d58-40a9-b0db-494d19a7bb4d-rte > div > div > iframe")
    #endregion

    #region Amputações
    # downloadVideoClass(driver,"#learning-module-title-_13753_1"
    #             ,"#learning-module-contents-_13753_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-253.makeStylescontentList-0-2-398 > div:nth-child(1) > div > div > div.makeStylescontentItemComponent-0-2-267 > div > div.makeStylescontentItemContentArea-0-2-270 > div.makeStylescontainer-0-2-304 > a"
    #             ,"#bbml-editor-id_8cc959a9-c978-4e53-b2f7-61e6c25955e6-rte > div > div > iframe#bbml-editor-id_8cc959a9-c978-4e53-b2f7-61e6c25955e6-rte > div > div > iframe")

    # downloadVideoClass(driver,""
    #             ,"#learning-module-contents-_13753_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-253.makeStylescontentList-0-2-398 > div:nth-child(2) > div > div > div.makeStylescontentItemComponent-0-2-267 > div > div.makeStylescontentItemContentArea-0-2-270 > div.makeStylescontainer-0-2-304 > a"
    #             ,"#bbml-editor-id_fa0097a3-4e6e-43fb-a3f4-3ea4a603c324-rte > div > div > iframe")
    #endregion

    #region Intensivismo
    # downloadVideoClass(driver,"#learning-module-title-_23879_1"
    #             ,"#learning-module-contents-_23879_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-253.makeStylescontentList-0-2-441 > div:nth-child(1) > div > div"
    #             ,"#bbml-editor-id_bb1a0ba4-44c5-4d56-a994-4b034239c1a5-rte > div > div > iframe#bbml-editor-id_bb1a0ba4-44c5-4d56-a994-4b034239c1a5-rte > div > div > iframe#bbml-editor-id_bb1a0ba4-44c5-4d56-a994-4b034239c1a5-rte > div > div > iframe")

    # downloadVideoClass(driver,""
    #             ,"#learning-module-contents-_23879_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-253.makeStylescontentList-0-2-441 > div:nth-child(2) > div > div"
    #             ,"#bbml-editor-id_f5023a87-9f5d-4342-b037-26b119c239ae-rte > div > div > iframe")

    # downloadVideo(driver,""
    #             ,"#learning-module-contents-_23879_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-253.makeStylescontentList-0-2-441 > div:nth-child(3) > div > div"
    #             ,"#bbml-editor-id_149cd16c-13ec-4450-b744-c15c5ebb60ff-rte > div > div > iframe")

    # downloadVideo(driver,""
    #             ,"#learning-module-contents-_23879_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-253.makeStylescontentList-0-2-441 > div:nth-child(4) > div > div"
    #             ,"#bbml-editor-id_606038e2-4feb-4d20-95cc-da575c63d5c2-rte > div > div > iframe")

    # downloadVideo(driver,""
    #             ,"#learning-module-contents-_23879_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-253.makeStylescontentList-0-2-441 > div:nth-child(8) > div > div"
    #             ,"#bbml-editor-id_f42c1f46-4ae6-4f22-ac34-63bc0f058797-rte > div > div > iframe")
    #endregion

    #region Antimicrobianos
    # downloadVideo(driver,"#learning-module-title-_28197_1"
    #             ,"#learning-module-contents-_28197_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-253.makeStylescontentList-0-2-527 > div:nth-child(1) > div > div > div.makeStylescontentItemComponent-0-2-267 > div > div.makeStylescontentItemContentArea-0-2-270 > div.makeStylescontainer-0-2-304 > a"
    #             ,"#bbml-editor-id_c91176a9-5a7f-423e-8f79-86e07d4e21e6-rte > div > div > iframe")

    # downloadVideo(driver,""
    #             ,"#learning-module-contents-_28197_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-253.makeStylescontentList-0-2-527 > div:nth-child(2) > div > div > div.makeStylescontentItemComponent-0-2-267 > div > div.makeStylescontentItemContentArea-0-2-270 > div.makeStylescontainer-0-2-304 > a"
    #             ,"#bbml-editor-id_5444c10a-8725-4a08-a530-c0deece51c73-rte > div > div > iframe")
    #endregion

    # region Infecção Relacionada à Assistência em Saúde (IRAS)
    # downloadVideoClass(driver,"#learning-module-title-_29144_1"
    #             ,"body > div#site-wrap.off-canvas-wrap:nth-child(2) > div.inner-wrap:nth-child(2) > bb-base-layout:nth-child(2) > div.base > main#main-content.bb-offcanvas-container:nth-child(3) > div.first.bb-offcanvas-panel.bb-offcanvas-right.full.with-banner.hide-in-background.active.cc_25_1.panel-has-focus:nth-child(3) > div.bb-offcanvas-panel-wrap > div.side-panel-content:nth-child(2) > div:nth-child(1) > div > div.course.courseConversion.course-color-7 > div.course-content-container:nth-child(1) > div.panel-wrap > div.panel-content:nth-child(4) > div.course-tool-content:nth-child(4) > div > div.course-outline.webkit-render-issue-fix.no-create:nth-child(2) > div.course-outline-row.row:nth-child(2) > div.columns.medium-12.large-9.outline-column.dropzoneTarget:nth-child(2) > div.element-card-list.js-content-outline:nth-child(3) > course-content-outline:nth-child(4) > react-course-content-outline.react-container > div > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-315:nth-child(2) > div.root.content-list-item.makeStylescontentListItem-0-2-313:nth-child(10) > div.makeStylescontainer-0-2-318 > div > div.MuiCollapsecontainer-0-2-368.MuiCollapseentered-0-2-369:nth-child(2) > div.MuiCollapsewrapper-0-2-371 > div.MuiCollapsewrapperInner-0-2-372.makeStyleslearningModuleContents-0-2-319 > div#learning-module-contents-_29144_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-455:nth-child(2) > div.content-list-item.makeStylescontentListItem-0-2-313:nth-child(1) > div.itemContainer > div.click-to-invoke-container.makeStylescontentItem-0-2-347.makeStylesnesting-0-2-355.makeStylesnesting-0-2-458.makeStylesclickable-0-2-348 > div.makeStylescontentItemComponent-0-2-323:nth-child(2) > div.makeStylescontentItemComponentDetails-0-2-324 > div.makeStylescontentItemContentArea-0-2-326:nth-child(1) > div.makeStylescontainer-0-2-360 > a"
    #             ,"iframe.no-select")
                
    # downloadVideoClass(driver,""
    #             ,"body > div#site-wrap.off-canvas-wrap:nth-child(2) > div.inner-wrap:nth-child(2) > bb-base-layout:nth-child(2) > div.base > main#main-content.bb-offcanvas-container:nth-child(3) > div.first.bb-offcanvas-panel.bb-offcanvas-right.full.with-banner.hide-in-background.active.cc_25_1.panel-has-focus:nth-child(3) > div.bb-offcanvas-panel-wrap > div.side-panel-content:nth-child(2) > div:nth-child(1) > div > div.course.courseConversion.course-color-7 > div.course-content-container:nth-child(1) > div.panel-wrap > div.panel-content:nth-child(4) > div.course-tool-content:nth-child(4) > div > div.course-outline.webkit-render-issue-fix.no-create:nth-child(2) > div.course-outline-row.row:nth-child(2) > div.columns.medium-12.large-9.outline-column.dropzoneTarget:nth-child(2) > div.element-card-list.js-content-outline:nth-child(3) > course-content-outline:nth-child(4) > react-course-content-outline.react-container > div > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-315:nth-child(2) > div.root.content-list-item.makeStylescontentListItem-0-2-313:nth-child(10) > div.makeStylescontainer-0-2-318 > div > div.MuiCollapsecontainer-0-2-368.MuiCollapseentered-0-2-369:nth-child(2) > div.MuiCollapsewrapper-0-2-371 > div.MuiCollapsewrapperInner-0-2-372.makeStyleslearningModuleContents-0-2-319 > div#learning-module-contents-_29144_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-455:nth-child(2) > div.content-list-item.makeStylescontentListItem-0-2-313:nth-child(2) > div.itemContainer > div.click-to-invoke-container.makeStylescontentItem-0-2-347.makeStylesnesting-0-2-355.makeStylesnesting-0-2-462.makeStylesclickable-0-2-348 > div.makeStylescontentItemComponent-0-2-323:nth-child(2) > div.makeStylescontentItemComponentDetails-0-2-324 > div.makeStylescontentItemContentArea-0-2-326:nth-child(1) > div.makeStylescontainer-0-2-360 > a"
    #             ,"iframe.no-select")

    # downloadVideoClass(driver,""
    #             ,"body > div#site-wrap.off-canvas-wrap:nth-child(2) > div.inner-wrap:nth-child(2) > bb-base-layout:nth-child(2) > div.base > main#main-content.bb-offcanvas-container:nth-child(3) > div.first.bb-offcanvas-panel.bb-offcanvas-right.full.with-banner.hide-in-background.active.cc_25_1.panel-has-focus:nth-child(3) > div.bb-offcanvas-panel-wrap > div.side-panel-content:nth-child(2) > div:nth-child(1) > div > div.course.courseConversion.course-color-7 > div.course-content-container:nth-child(1) > div.panel-wrap > div.panel-content:nth-child(4) > div.course-tool-content:nth-child(4) > div > div.course-outline.webkit-render-issue-fix.no-create:nth-child(2) > div.course-outline-row.row:nth-child(2) > div.columns.medium-12.large-9.outline-column.dropzoneTarget:nth-child(2) > div.element-card-list.js-content-outline:nth-child(3) > course-content-outline:nth-child(4) > react-course-content-outline.react-container > div > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-315:nth-child(2) > div.root.content-list-item.makeStylescontentListItem-0-2-313:nth-child(10) > div.makeStylescontainer-0-2-318 > div > div.MuiCollapsecontainer-0-2-368.MuiCollapseentered-0-2-369:nth-child(2) > div.MuiCollapsewrapper-0-2-371 > div.MuiCollapsewrapperInner-0-2-372.makeStyleslearningModuleContents-0-2-319 > div#learning-module-contents-_29144_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-455:nth-child(2) > div.content-list-item.makeStylescontentListItem-0-2-313:nth-child(3) > div.itemContainer > div.click-to-invoke-container.makeStylescontentItem-0-2-347.makeStylesnesting-0-2-355.makeStylesnesting-0-2-464.makeStylesclickable-0-2-348 > div.makeStylescontentItemComponent-0-2-323:nth-child(2) > div.makeStylescontentItemComponentDetails-0-2-324 > div.makeStylescontentItemContentArea-0-2-326:nth-child(1) > div.makeStylescontainer-0-2-360 > a"
    #             ,"iframe.no-select")

    # downloadVideoClass(driver,""
    #             ,"body > div#site-wrap.off-canvas-wrap:nth-child(2) > div.inner-wrap:nth-child(2) > bb-base-layout:nth-child(2) > div.base > main#main-content.bb-offcanvas-container:nth-child(3) > div.first.bb-offcanvas-panel.bb-offcanvas-right.full.with-banner.hide-in-background.active.cc_25_1.panel-has-focus:nth-child(3) > div.bb-offcanvas-panel-wrap > div.side-panel-content:nth-child(2) > div:nth-child(1) > div > div.course.courseConversion.course-color-7 > div.course-content-container:nth-child(1) > div.panel-wrap > div.panel-content:nth-child(4) > div.course-tool-content:nth-child(4) > div > div.course-outline.webkit-render-issue-fix.no-create:nth-child(2) > div.course-outline-row.row:nth-child(2) > div.columns.medium-12.large-9.outline-column.dropzoneTarget:nth-child(2) > div.element-card-list.js-content-outline:nth-child(3) > course-content-outline:nth-child(4) > react-course-content-outline.react-container > div > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-315:nth-child(2) > div.root.content-list-item.makeStylescontentListItem-0-2-313:nth-child(10) > div.makeStylescontainer-0-2-318 > div > div.MuiCollapsecontainer-0-2-368.MuiCollapseentered-0-2-369:nth-child(2) > div.MuiCollapsewrapper-0-2-371 > div.MuiCollapsewrapperInner-0-2-372.makeStyleslearningModuleContents-0-2-319 > div#learning-module-contents-_29144_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-455:nth-child(2) > div.content-list-item.makeStylescontentListItem-0-2-313:nth-child(4) > div.itemContainer > div.click-to-invoke-container.makeStylescontentItem-0-2-347.makeStylesnesting-0-2-355.makeStylesnesting-0-2-466.makeStylesclickable-0-2-348 > div.makeStylescontentItemComponent-0-2-323:nth-child(2) > div.makeStylescontentItemComponentDetails-0-2-324 > div.makeStylescontentItemContentArea-0-2-326:nth-child(1) > div.makeStylescontainer-0-2-360"
    #             ,"iframe.no-select")

    # downloadVideoClass(driver,""
    #             ,"body > div#site-wrap.off-canvas-wrap:nth-child(2) > div.inner-wrap:nth-child(2) > bb-base-layout:nth-child(2) > div.base > main#main-content.bb-offcanvas-container:nth-child(3) > div.first.bb-offcanvas-panel.bb-offcanvas-right.full.with-banner.hide-in-background.active.cc_25_1.panel-has-focus:nth-child(3) > div.bb-offcanvas-panel-wrap > div.side-panel-content:nth-child(2) > div:nth-child(1) > div > div.course.courseConversion.course-color-7 > div.course-content-container:nth-child(1) > div.panel-wrap > div.panel-content:nth-child(4) > div.course-tool-content:nth-child(4) > div > div.course-outline.webkit-render-issue-fix.no-create:nth-child(2) > div.course-outline-row.row:nth-child(2) > div.columns.medium-12.large-9.outline-column.dropzoneTarget:nth-child(2) > div.element-card-list.js-content-outline:nth-child(3) > course-content-outline:nth-child(4) > react-course-content-outline.react-container > div > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-315:nth-child(2) > div.root.content-list-item.makeStylescontentListItem-0-2-313:nth-child(10) > div.makeStylescontainer-0-2-318 > div > div.MuiCollapsecontainer-0-2-368.MuiCollapseentered-0-2-369:nth-child(2) > div.MuiCollapsewrapper-0-2-371 > div.MuiCollapsewrapperInner-0-2-372.makeStyleslearningModuleContents-0-2-319 > div#learning-module-contents-_29144_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-455:nth-child(2) > div.content-list-item.makeStylescontentListItem-0-2-313:nth-child(5) > div.itemContainer > div.click-to-invoke-container.makeStylescontentItem-0-2-347.makeStylesnesting-0-2-355.makeStylesnesting-0-2-466.makeStylesclickable-0-2-348 > div.makeStylescontentItemComponent-0-2-323:nth-child(2) > div.makeStylescontentItemComponentDetails-0-2-324 > div.makeStylescontentItemContentArea-0-2-326:nth-child(1) > div.makeStylescontainer-0-2-360"
    #             ,"iframe.no-select")

    # downloadVideoClass(driver,""
    #             ,"body > div#site-wrap.off-canvas-wrap:nth-child(2) > div.inner-wrap:nth-child(2) > bb-base-layout:nth-child(2) > div.base > main#main-content.bb-offcanvas-container:nth-child(3) > div.first.bb-offcanvas-panel.bb-offcanvas-right.full.with-banner.hide-in-background.active.cc_25_1.panel-has-focus:nth-child(3) > div.bb-offcanvas-panel-wrap > div.side-panel-content:nth-child(2) > div:nth-child(1) > div > div.course.courseConversion.course-color-7 > div.course-content-container:nth-child(1) > div.panel-wrap > div.panel-content:nth-child(4) > div.course-tool-content:nth-child(4) > div > div.course-outline.webkit-render-issue-fix.no-create:nth-child(2) > div.course-outline-row.row:nth-child(2) > div.columns.medium-12.large-9.outline-column.dropzoneTarget:nth-child(2) > div.element-card-list.js-content-outline:nth-child(3) > course-content-outline:nth-child(4) > react-course-content-outline.react-container > div > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-315:nth-child(2) > div.root.content-list-item.makeStylescontentListItem-0-2-313:nth-child(10) > div.makeStylescontainer-0-2-318 > div > div.MuiCollapsecontainer-0-2-368.MuiCollapseentered-0-2-369:nth-child(2) > div.MuiCollapsewrapper-0-2-371 > div.MuiCollapsewrapperInner-0-2-372.makeStyleslearningModuleContents-0-2-319 > div#learning-module-contents-_29144_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-455:nth-child(2) > div.content-list-item.makeStylescontentListItem-0-2-313:nth-child(6) > div.itemContainer > div.click-to-invoke-container.makeStylescontentItem-0-2-347.makeStylesnesting-0-2-355.makeStylesnesting-0-2-466.makeStylesclickable-0-2-348 > div.makeStylescontentItemComponent-0-2-323:nth-child(2) > div.makeStylescontentItemComponentDetails-0-2-324 > div.makeStylescontentItemContentArea-0-2-326:nth-child(1) > div.makeStylescontainer-0-2-360"
    #             ,"iframe.no-select")

    # downloadVideoClass(driver,""
    #             ,"body > div#site-wrap.off-canvas-wrap:nth-child(2) > div.inner-wrap:nth-child(2) > bb-base-layout:nth-child(2) > div.base > main#main-content.bb-offcanvas-container:nth-child(3) > div.first.bb-offcanvas-panel.bb-offcanvas-right.full.with-banner.hide-in-background.active.cc_25_1.panel-has-focus:nth-child(3) > div.bb-offcanvas-panel-wrap > div.side-panel-content:nth-child(2) > div:nth-child(1) > div > div.course.courseConversion.course-color-7 > div.course-content-container:nth-child(1) > div.panel-wrap > div.panel-content:nth-child(4) > div.course-tool-content:nth-child(4) > div > div.course-outline.webkit-render-issue-fix.no-create:nth-child(2) > div.course-outline-row.row:nth-child(2) > div.columns.medium-12.large-9.outline-column.dropzoneTarget:nth-child(2) > div.element-card-list.js-content-outline:nth-child(3) > course-content-outline:nth-child(4) > react-course-content-outline.react-container > div > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-315:nth-child(2) > div.root.content-list-item.makeStylescontentListItem-0-2-313:nth-child(10) > div.makeStylescontainer-0-2-318 > div > div.MuiCollapsecontainer-0-2-368.MuiCollapseentered-0-2-369:nth-child(2) > div.MuiCollapsewrapper-0-2-371 > div.MuiCollapsewrapperInner-0-2-372.makeStyleslearningModuleContents-0-2-319 > div#learning-module-contents-_29144_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-455:nth-child(2) > div.content-list-item.makeStylescontentListItem-0-2-313:nth-child(8) > div.itemContainer > div.click-to-invoke-container.makeStylescontentItem-0-2-347.makeStylesnesting-0-2-355.makeStylesnesting-0-2-466.makeStylesclickable-0-2-348 > div.makeStylescontentItemComponent-0-2-323:nth-child(2) > div.makeStylescontentItemComponentDetails-0-2-324 > div.makeStylescontentItemContentArea-0-2-326:nth-child(1) > div.makeStylescontainer-0-2-360"
    #             ,"iframe.no-select")

    # downloadVideoClass(driver,""
    #             ,"body > div#site-wrap.off-canvas-wrap:nth-child(2) > div.inner-wrap:nth-child(2) > bb-base-layout:nth-child(2) > div.base > main#main-content.bb-offcanvas-container:nth-child(3) > div.first.bb-offcanvas-panel.bb-offcanvas-right.full.with-banner.hide-in-background.active.cc_25_1.panel-has-focus:nth-child(3) > div.bb-offcanvas-panel-wrap > div.side-panel-content:nth-child(2) > div:nth-child(1) > div > div.course.courseConversion.course-color-7 > div.course-content-container:nth-child(1) > div.panel-wrap > div.panel-content:nth-child(4) > div.course-tool-content:nth-child(4) > div > div.course-outline.webkit-render-issue-fix.no-create:nth-child(2) > div.course-outline-row.row:nth-child(2) > div.columns.medium-12.large-9.outline-column.dropzoneTarget:nth-child(2) > div.element-card-list.js-content-outline:nth-child(3) > course-content-outline:nth-child(4) > react-course-content-outline.react-container > div > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-315:nth-child(2) > div.root.content-list-item.makeStylescontentListItem-0-2-313:nth-child(10) > div.makeStylescontainer-0-2-318 > div > div.MuiCollapsecontainer-0-2-368.MuiCollapseentered-0-2-369:nth-child(2) > div.MuiCollapsewrapper-0-2-371 > div.MuiCollapsewrapperInner-0-2-372.makeStyleslearningModuleContents-0-2-319 > div#learning-module-contents-_29144_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-455:nth-child(2) > div.content-list-item.makeStylescontentListItem-0-2-313:nth-child(8) > div.itemContainer > div.click-to-invoke-container.makeStylescontentItem-0-2-347.makeStylesnesting-0-2-355.makeStylesnesting-0-2-466.makeStylesclickable-0-2-348 > div.makeStylescontentItemComponent-0-2-323:nth-child(2) > div.makeStylescontentItemComponentDetails-0-2-324 > div.makeStylescontentItemContentArea-0-2-326:nth-child(1) > div.makeStylescontainer-0-2-360"
    #             ,"iframe.no-select")
    #endregion

    # region Prática de acesso ao abdomen
    # print('start Prática de acesso ao abdomen')

    # downloadVideoClass(driver,"#learning-module-title-_24563_1"
    #             ,"body > div#site-wrap.off-canvas-wrap:nth-child(2) > div.inner-wrap:nth-child(2) > bb-base-layout:nth-child(2) > div.base > main#main-content.bb-offcanvas-container:nth-child(3) > div.first.bb-offcanvas-panel.bb-offcanvas-right.full.with-banner.hide-in-background.active.cc_25_1.panel-has-focus:nth-child(3) > div.bb-offcanvas-panel-wrap > div.side-panel-content:nth-child(2) > div:nth-child(1) > div > div.course.courseConversion.course-color-7 > div.course-content-container:nth-child(1) > div.panel-wrap > div.panel-content:nth-child(4) > div.course-tool-content:nth-child(4) > div > div.course-outline.webkit-render-issue-fix.no-create:nth-child(2) > div.course-outline-row.row:nth-child(2) > div.columns.medium-12.large-9.outline-column.dropzoneTarget:nth-child(2) > div.element-card-list.js-content-outline:nth-child(3) > course-content-outline:nth-child(4) > react-course-content-outline.react-container > div > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-315:nth-child(2) > div.root.content-list-item.makeStylescontentListItem-0-2-313:nth-child(11) > div.makeStylescontainer-0-2-318 > div > div.MuiCollapsecontainer-0-2-368.MuiCollapseentered-0-2-369:nth-child(2) > div.MuiCollapsewrapper-0-2-371 > div.MuiCollapsewrapperInner-0-2-372.makeStyleslearningModuleContents-0-2-319 > div#learning-module-contents-_24563_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-490:nth-child(2) > div.content-list-item.makeStylescontentListItem-0-2-313:nth-child(1) > div.itemContainer > div.click-to-invoke-container.makeStylescontentItem-0-2-347.makeStylesnesting-0-2-355.makeStylesnesting-0-2-493.makeStylesclickable-0-2-348 > div.makeStylescontentItemComponent-0-2-323:nth-child(2) > div.makeStylescontentItemComponentDetails-0-2-324 > div.makeStylescontentItemContentArea-0-2-326:nth-child(1) > div.makeStylescontainer-0-2-360:nth-child(1) > a"
    #             ,"iframe.no-select")

    # downloadVideoClass(driver,""
    #             ,"body > div#site-wrap.off-canvas-wrap:nth-child(2) > div.inner-wrap:nth-child(2) > bb-base-layout:nth-child(2) > div.base > main#main-content.bb-offcanvas-container:nth-child(3) > div.first.bb-offcanvas-panel.bb-offcanvas-right.full.with-banner.hide-in-background.active.cc_25_1.panel-has-focus:nth-child(3) > div.bb-offcanvas-panel-wrap > div.side-panel-content:nth-child(2) > div:nth-child(1) > div > div.course.courseConversion.course-color-7 > div.course-content-container:nth-child(1) > div.panel-wrap > div.panel-content:nth-child(4) > div.course-tool-content:nth-child(4) > div > div.course-outline.webkit-render-issue-fix.no-create:nth-child(2) > div.course-outline-row.row:nth-child(2) > div.columns.medium-12.large-9.outline-column.dropzoneTarget:nth-child(2) > div.element-card-list.js-content-outline:nth-child(3) > course-content-outline:nth-child(4) > react-course-content-outline.react-container > div > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-315:nth-child(2) > div.root.content-list-item.makeStylescontentListItem-0-2-313:nth-child(11) > div.makeStylescontainer-0-2-318 > div > div.MuiCollapsecontainer-0-2-368.MuiCollapseentered-0-2-369:nth-child(2) > div.MuiCollapsewrapper-0-2-371 > div.MuiCollapsewrapperInner-0-2-372.makeStyleslearningModuleContents-0-2-319 > div#learning-module-contents-_24563_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-490:nth-child(2) > div.content-list-item.makeStylescontentListItem-0-2-313:nth-child(2) > div.itemContainer > div.click-to-invoke-container.makeStylescontentItem-0-2-347.makeStylesnesting-0-2-355.makeStylesnesting-0-2-495.makeStylesclickable-0-2-348 > div.makeStylescontentItemComponent-0-2-323:nth-child(2) > div.makeStylescontentItemComponentDetails-0-2-324 > div.makeStylescontentItemContentArea-0-2-326:nth-child(1) > div.makeStylescontainer-0-2-360:nth-child(1)"
    #             ,"iframe.no-select")

    # downloadVideoClass(driver,""
    #             ,"body > div#site-wrap.off-canvas-wrap:nth-child(2) > div.inner-wrap:nth-child(2) > bb-base-layout:nth-child(2) > div.base > main#main-content.bb-offcanvas-container:nth-child(3) > div.first.bb-offcanvas-panel.bb-offcanvas-right.full.with-banner.hide-in-background.active.cc_25_1.panel-has-focus:nth-child(3) > div.bb-offcanvas-panel-wrap > div.side-panel-content:nth-child(2) > div:nth-child(1) > div > div.course.courseConversion.course-color-7 > div.course-content-container:nth-child(1) > div.panel-wrap > div.panel-content:nth-child(4) > div.course-tool-content:nth-child(4) > div > div.course-outline.webkit-render-issue-fix.no-create:nth-child(2) > div.course-outline-row.row:nth-child(2) > div.columns.medium-12.large-9.outline-column.dropzoneTarget:nth-child(2) > div.element-card-list.js-content-outline:nth-child(3) > course-content-outline:nth-child(4) > react-course-content-outline.react-container > div > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-315:nth-child(2) > div.root.content-list-item.makeStylescontentListItem-0-2-313:nth-child(11) > div.makeStylescontainer-0-2-318 > div > div.MuiCollapsecontainer-0-2-368.MuiCollapseentered-0-2-369:nth-child(2) > div.MuiCollapsewrapper-0-2-371 > div.MuiCollapsewrapperInner-0-2-372.makeStyleslearningModuleContents-0-2-319 > div#learning-module-contents-_24563_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-490:nth-child(2) > div.content-list-item.makeStylescontentListItem-0-2-313:nth-child(3) > div.itemContainer > div.click-to-invoke-container.makeStylescontentItem-0-2-347.makeStylesnesting-0-2-355.makeStylesnesting-0-2-497.makeStylesclickable-0-2-348 > div.makeStylescontentItemComponent-0-2-323:nth-child(2) > div.makeStylescontentItemComponentDetails-0-2-324 > div.makeStylescontentItemContentArea-0-2-326:nth-child(1) > div.makeStylescontainer-0-2-360:nth-child(1)"
    #             ,"iframe.no-select")

    # downloadVideoClass(driver,""
    #             ,"body > div#site-wrap.off-canvas-wrap:nth-child(2) > div.inner-wrap:nth-child(2) > bb-base-layout:nth-child(2) > div.base > main#main-content.bb-offcanvas-container:nth-child(3) > div.first.bb-offcanvas-panel.bb-offcanvas-right.full.with-banner.hide-in-background.active.cc_25_1.panel-has-focus:nth-child(3) > div.bb-offcanvas-panel-wrap > div.side-panel-content:nth-child(2) > div:nth-child(1) > div > div.course.courseConversion.course-color-7 > div.course-content-container:nth-child(1) > div.panel-wrap > div.panel-content:nth-child(4) > div.course-tool-content:nth-child(4) > div > div.course-outline.webkit-render-issue-fix.no-create:nth-child(2) > div.course-outline-row.row:nth-child(2) > div.columns.medium-12.large-9.outline-column.dropzoneTarget:nth-child(2) > div.element-card-list.js-content-outline:nth-child(3) > course-content-outline:nth-child(4) > react-course-content-outline.react-container > div > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-315:nth-child(2) > div.root.content-list-item.makeStylescontentListItem-0-2-313:nth-child(11) > div.makeStylescontainer-0-2-318 > div > div.MuiCollapsecontainer-0-2-368.MuiCollapseentered-0-2-369:nth-child(2) > div.MuiCollapsewrapper-0-2-371 > div.MuiCollapsewrapperInner-0-2-372.makeStyleslearningModuleContents-0-2-319 > div#learning-module-contents-_24563_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-490:nth-child(2) > div.content-list-item.makeStylescontentListItem-0-2-313:nth-child(4) > div.itemContainer > div.click-to-invoke-container.makeStylescontentItem-0-2-347.makeStylesnesting-0-2-355.makeStylesnesting-0-2-499.makeStylesclickable-0-2-348 > div.makeStylescontentItemComponent-0-2-323:nth-child(2) > div.makeStylescontentItemComponentDetails-0-2-324 > div.makeStylescontentItemContentArea-0-2-326:nth-child(1) > div.makeStylescontainer-0-2-360:nth-child(1)"
    #             ,"iframe.no-select")

    # downloadVideoClass(driver,""
    #             ,"body > div#site-wrap.off-canvas-wrap:nth-child(2) > div.inner-wrap:nth-child(2) > bb-base-layout:nth-child(2) > div.base > main#main-content.bb-offcanvas-container:nth-child(3) > div.first.bb-offcanvas-panel.bb-offcanvas-right.full.with-banner.hide-in-background.active.cc_25_1.panel-has-focus:nth-child(3) > div.bb-offcanvas-panel-wrap > div.side-panel-content:nth-child(2) > div:nth-child(1) > div > div.course.courseConversion.course-color-7 > div.course-content-container:nth-child(1) > div.panel-wrap > div.panel-content:nth-child(4) > div.course-tool-content:nth-child(4) > div > div.course-outline.webkit-render-issue-fix.no-create:nth-child(2) > div.course-outline-row.row:nth-child(2) > div.columns.medium-12.large-9.outline-column.dropzoneTarget:nth-child(2) > div.element-card-list.js-content-outline:nth-child(3) > course-content-outline:nth-child(4) > react-course-content-outline.react-container > div > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-315:nth-child(2) > div.root.content-list-item.makeStylescontentListItem-0-2-313:nth-child(11) > div.makeStylescontainer-0-2-318 > div > div.MuiCollapsecontainer-0-2-368.MuiCollapseentered-0-2-369:nth-child(2) > div.MuiCollapsewrapper-0-2-371 > div.MuiCollapsewrapperInner-0-2-372.makeStyleslearningModuleContents-0-2-319 > div#learning-module-contents-_24563_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-490:nth-child(2) > div.content-list-item.makeStylescontentListItem-0-2-313:nth-child(5) > div.itemContainer > div.click-to-invoke-container.makeStylescontentItem-0-2-347.makeStylesnesting-0-2-355.makeStylesnesting-0-2-501.makeStylesclickable-0-2-348 > div.makeStylescontentItemComponent-0-2-323:nth-child(2) > div.makeStylescontentItemComponentDetails-0-2-324 > div.makeStylescontentItemContentArea-0-2-326:nth-child(1) > div.makeStylescontainer-0-2-360:nth-child(1)"
    #             ,"iframe.no-select")
    # endregion

    # region Prática de amputações
    # print('Prática de Amputações')
    # downloadVideoClass(driver,"#learning-module-title-_24564_1"
    #             ,"body > div#site-wrap.off-canvas-wrap:nth-child(2) > div.inner-wrap:nth-child(2) > bb-base-layout:nth-child(2) > div.base > main#main-content.bb-offcanvas-container:nth-child(3) > div.first.bb-offcanvas-panel.bb-offcanvas-right.full.with-banner.hide-in-background.active.cc_25_1.panel-has-focus:nth-child(3) > div.bb-offcanvas-panel-wrap > div.side-panel-content:nth-child(2) > div:nth-child(1) > div > div.course.courseConversion.course-color-7 > div.course-content-container:nth-child(1) > div.panel-wrap > div.panel-content:nth-child(4) > div.course-tool-content:nth-child(4) > div > div.course-outline.webkit-render-issue-fix.no-create:nth-child(2) > div.course-outline-row.row:nth-child(2) > div.columns.medium-12.large-9.outline-column.dropzoneTarget:nth-child(2) > div.element-card-list.js-content-outline:nth-child(3) > course-content-outline:nth-child(4) > react-course-content-outline.react-container > div > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-315:nth-child(2) > div.root.content-list-item.makeStylescontentListItem-0-2-313:nth-child(12) > div.makeStylescontainer-0-2-318 > div > div.MuiCollapsecontainer-0-2-368.MuiCollapseentered-0-2-369:nth-child(2) > div.MuiCollapsewrapper-0-2-371 > div.MuiCollapsewrapperInner-0-2-372.makeStyleslearningModuleContents-0-2-319 > div#learning-module-contents-_24564_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-519:nth-child(2) > div.content-list-item.makeStylescontentListItem-0-2-313:nth-child(1) > div.itemContainer > div.click-to-invoke-container.makeStylescontentItem-0-2-347.makeStylesnesting-0-2-355.makeStylesnesting-0-2-522.makeStylesclickable-0-2-348 > div.makeStylescontentItemComponent-0-2-323:nth-child(2) > div.makeStylescontentItemComponentDetails-0-2-324 > div.makeStylescontentItemContentArea-0-2-326:nth-child(1) > div.makeStylescontainer-0-2-360:nth-child(1)"
    #             ,"iframe.no-select")

    # downloadVideoClass(driver,""
    #             ,"body > div#site-wrap.off-canvas-wrap:nth-child(2) > div.inner-wrap:nth-child(2) > bb-base-layout:nth-child(2) > div.base > main#main-content.bb-offcanvas-container:nth-child(3) > div.first.bb-offcanvas-panel.bb-offcanvas-right.full.with-banner.hide-in-background.active.cc_25_1.panel-has-focus:nth-child(3) > div.bb-offcanvas-panel-wrap > div.side-panel-content:nth-child(2) > div:nth-child(1) > div > div.course.courseConversion.course-color-7 > div.course-content-container:nth-child(1) > div.panel-wrap > div.panel-content:nth-child(4) > div.course-tool-content:nth-child(4) > div > div.course-outline.webkit-render-issue-fix.no-create:nth-child(2) > div.course-outline-row.row:nth-child(2) > div.columns.medium-12.large-9.outline-column.dropzoneTarget:nth-child(2) > div.element-card-list.js-content-outline:nth-child(3) > course-content-outline:nth-child(4) > react-course-content-outline.react-container > div > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-315:nth-child(2) > div.root.content-list-item.makeStylescontentListItem-0-2-313:nth-child(12) > div.makeStylescontainer-0-2-318 > div > div.MuiCollapsecontainer-0-2-368.MuiCollapseentered-0-2-369:nth-child(2) > div.MuiCollapsewrapper-0-2-371 > div.MuiCollapsewrapperInner-0-2-372.makeStyleslearningModuleContents-0-2-319 > div#learning-module-contents-_24564_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-519:nth-child(2) > div.content-list-item.makeStylescontentListItem-0-2-313:nth-child(2) > div.itemContainer > div.click-to-invoke-container.makeStylescontentItem-0-2-347.makeStylesnesting-0-2-355.makeStylesnesting-0-2-526.makeStylesclickable-0-2-348 > div.makeStylescontentItemComponent-0-2-323:nth-child(2) > div.makeStylescontentItemComponentDetails-0-2-324 > div.makeStylescontentItemContentArea-0-2-326:nth-child(1) > div.makeStylescontainer-0-2-360:nth-child(1)"
    #             ,"iframe.no-select")

    # downloadVideoClass(driver,""
    #             ,"body > div#site-wrap.off-canvas-wrap:nth-child(2) > div.inner-wrap:nth-child(2) > bb-base-layout:nth-child(2) > div.base > main#main-content.bb-offcanvas-container:nth-child(3) > div.first.bb-offcanvas-panel.bb-offcanvas-right.full.with-banner.hide-in-background.active.cc_25_1.panel-has-focus:nth-child(3) > div.bb-offcanvas-panel-wrap > div.side-panel-content:nth-child(2) > div:nth-child(1) > div > div.course.courseConversion.course-color-7 > div.course-content-container:nth-child(1) > div.panel-wrap > div.panel-content:nth-child(4) > div.course-tool-content:nth-child(4) > div > div.course-outline.webkit-render-issue-fix.no-create:nth-child(2) > div.course-outline-row.row:nth-child(2) > div.columns.medium-12.large-9.outline-column.dropzoneTarget:nth-child(2) > div.element-card-list.js-content-outline:nth-child(3) > course-content-outline:nth-child(4) > react-course-content-outline.react-container > div > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-315:nth-child(2) > div.root.content-list-item.makeStylescontentListItem-0-2-313:nth-child(12) > div.makeStylescontainer-0-2-318 > div > div.MuiCollapsecontainer-0-2-368.MuiCollapseentered-0-2-369:nth-child(2) > div.MuiCollapsewrapper-0-2-371 > div.MuiCollapsewrapperInner-0-2-372.makeStyleslearningModuleContents-0-2-319 > div#learning-module-contents-_24564_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-519:nth-child(2) > div.content-list-item.makeStylescontentListItem-0-2-313:nth-child(3) > div.itemContainer > div.click-to-invoke-container.makeStylescontentItem-0-2-347.makeStylesnesting-0-2-355.makeStylesnesting-0-2-526.makeStylesclickable-0-2-348 > div.makeStylescontentItemComponent-0-2-323:nth-child(2) > div.makeStylescontentItemComponentDetails-0-2-324 > div.makeStylescontentItemContentArea-0-2-326:nth-child(1) > div.makeStylescontainer-0-2-360:nth-child(1)"
    #             ,"iframe.no-select")
    # downloadVideoClass(driver,""
    #             ,"body > div#site-wrap.off-canvas-wrap:nth-child(2) > div.inner-wrap:nth-child(2) > bb-base-layout:nth-child(2) > div.base > main#main-content.bb-offcanvas-container:nth-child(3) > div.first.bb-offcanvas-panel.bb-offcanvas-right.full.with-banner.hide-in-background.active.cc_25_1.panel-has-focus:nth-child(3) > div.bb-offcanvas-panel-wrap > div.side-panel-content:nth-child(2) > div:nth-child(1) > div > div.course.courseConversion.course-color-7 > div.course-content-container:nth-child(1) > div.panel-wrap > div.panel-content:nth-child(4) > div.course-tool-content:nth-child(4) > div > div.course-outline.webkit-render-issue-fix.no-create:nth-child(2) > div.course-outline-row.row:nth-child(2) > div.columns.medium-12.large-9.outline-column.dropzoneTarget:nth-child(2) > div.element-card-list.js-content-outline:nth-child(3) > course-content-outline:nth-child(4) > react-course-content-outline.react-container > div > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-315:nth-child(2) > div.root.content-list-item.makeStylescontentListItem-0-2-313:nth-child(12) > div.makeStylescontainer-0-2-318 > div > div.MuiCollapsecontainer-0-2-368.MuiCollapseentered-0-2-369:nth-child(2) > div.MuiCollapsewrapper-0-2-371 > div.MuiCollapsewrapperInner-0-2-372.makeStyleslearningModuleContents-0-2-319 > div#learning-module-contents-_24564_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-519:nth-child(2) > div.content-list-item.makeStylescontentListItem-0-2-313:nth-child(4) > div.itemContainer > div.click-to-invoke-container.makeStylescontentItem-0-2-347.makeStylesnesting-0-2-355.makeStylesnesting-0-2-526.makeStylesclickable-0-2-348 > div.makeStylescontentItemComponent-0-2-323:nth-child(2) > div.makeStylescontentItemComponentDetails-0-2-324 > div.makeStylescontentItemContentArea-0-2-326:nth-child(1) > div.makeStylescontainer-0-2-360:nth-child(1)"
    #             ,"iframe.no-select")

    # downloadVideoClass(driver,""
    #             ,"body > div#site-wrap.off-canvas-wrap:nth-child(2) > div.inner-wrap:nth-child(2) > bb-base-layout:nth-child(2) > div.base > main#main-content.bb-offcanvas-container:nth-child(3) > div.first.bb-offcanvas-panel.bb-offcanvas-right.full.with-banner.hide-in-background.active.cc_25_1.panel-has-focus:nth-child(3) > div.bb-offcanvas-panel-wrap > div.side-panel-content:nth-child(2) > div:nth-child(1) > div > div.course.courseConversion.course-color-7 > div.course-content-container:nth-child(1) > div.panel-wrap > div.panel-content:nth-child(4) > div.course-tool-content:nth-child(4) > div > div.course-outline.webkit-render-issue-fix.no-create:nth-child(2) > div.course-outline-row.row:nth-child(2) > div.columns.medium-12.large-9.outline-column.dropzoneTarget:nth-child(2) > div.element-card-list.js-content-outline:nth-child(3) > course-content-outline:nth-child(4) > react-course-content-outline.react-container > div > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-315:nth-child(2) > div.root.content-list-item.makeStylescontentListItem-0-2-313:nth-child(12) > div.makeStylescontainer-0-2-318 > div > div.MuiCollapsecontainer-0-2-368.MuiCollapseentered-0-2-369:nth-child(2) > div.MuiCollapsewrapper-0-2-371 > div.MuiCollapsewrapperInner-0-2-372.makeStyleslearningModuleContents-0-2-319 > div#learning-module-contents-_24564_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-519:nth-child(2) > div.content-list-item.makeStylescontentListItem-0-2-313:nth-child(5) > div.itemContainer > div.click-to-invoke-container.makeStylescontentItem-0-2-347.makeStylesnesting-0-2-355.makeStylesnesting-0-2-526.makeStylesclickable-0-2-348 > div.makeStylescontentItemComponent-0-2-323:nth-child(2) > div.makeStylescontentItemComponentDetails-0-2-324 > div.makeStylescontentItemContentArea-0-2-326:nth-child(1) > div.makeStylescontainer-0-2-360:nth-child(1)"
    #             ,"iframe.no-select")

    # downloadVideoClass(driver,""
    #             ,"body > div#site-wrap.off-canvas-wrap:nth-child(2) > div.inner-wrap:nth-child(2) > bb-base-layout:nth-child(2) > div.base > main#main-content.bb-offcanvas-container:nth-child(3) > div.first.bb-offcanvas-panel.bb-offcanvas-right.full.with-banner.hide-in-background.active.cc_25_1.panel-has-focus:nth-child(3) > div.bb-offcanvas-panel-wrap > div.side-panel-content:nth-child(2) > div:nth-child(1) > div > div.course.courseConversion.course-color-7 > div.course-content-container:nth-child(1) > div.panel-wrap > div.panel-content:nth-child(4) > div.course-tool-content:nth-child(4) > div > div.course-outline.webkit-render-issue-fix.no-create:nth-child(2) > div.course-outline-row.row:nth-child(2) > div.columns.medium-12.large-9.outline-column.dropzoneTarget:nth-child(2) > div.element-card-list.js-content-outline:nth-child(3) > course-content-outline:nth-child(4) > react-course-content-outline.react-container > div > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-315:nth-child(2) > div.root.content-list-item.makeStylescontentListItem-0-2-313:nth-child(12) > div.makeStylescontainer-0-2-318 > div > div.MuiCollapsecontainer-0-2-368.MuiCollapseentered-0-2-369:nth-child(2) > div.MuiCollapsewrapper-0-2-371 > div.MuiCollapsewrapperInner-0-2-372.makeStyleslearningModuleContents-0-2-319 > div#learning-module-contents-_24564_1 > div > div:nth-child(1) > div.makeStylescontentList-0-2-309.makeStylescontentList-0-2-519:nth-child(2) > div.content-list-item.makeStylescontentListItem-0-2-313:nth-child(6) > div.itemContainer > div.click-to-invoke-container.makeStylescontentItem-0-2-347.makeStylesnesting-0-2-355.makeStylesnesting-0-2-526.makeStylesclickable-0-2-348 > div.makeStylescontentItemComponent-0-2-323:nth-child(2) > div.makeStylescontentItemComponentDetails-0-2-324 > div.makeStylescontentItemContentArea-0-2-326:nth-child(1) > div.makeStylescontainer-0-2-360:nth-child(1)"
    #             ,"iframe.no-select")
    # endregion              
