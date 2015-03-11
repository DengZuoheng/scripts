// ==UserScript==
// @name         jnu study auto login
// @namespace    http://dengzuoheng.github.io
// @version      0.1
// @description  enter something useful
// @author       You
// @match        http://study.jnu.edu.cn/
// @grant        none
// @run-at       document-end
// ==/UserScript==
$("#user_id").val("2012052207");
$("#password").val("2012052207");
$("input[src='/webapps/bb-silkIII-bb_bb60/homepage/images/login_btn.jpg']").click();