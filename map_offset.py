


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>lbs/map_offset.py at master · brightman/lbs · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />

    
    

    <meta content="authenticity_token" name="csrf-param" />
<meta content="bf2dFftrrktH0d3MZzPP9frWOr3jb5NAs616Xzhh61U=" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/stylesheets/bundles/github-e2fb92c4dcb5e5b1ce2ffd0e84d6bf80937d9197.css" media="screen" rel="stylesheet" type="text/css" />
    <link href="https://a248.e.akamai.net/assets.github.com/stylesheets/bundles/github2-a6e03f3438e57a85fea8f7cc4939ed556a5c96e4.css" media="screen" rel="stylesheet" type="text/css" />
    

    <script src="https://a248.e.akamai.net/assets.github.com/javascripts/bundles/jquery-225576cef50ef2097c9f9fbcd8953c1572544611.js" type="text/javascript"></script>
    <script src="https://a248.e.akamai.net/assets.github.com/javascripts/bundles/github-353ded132c604f1bdf010516392d71052f37ffcf.js" type="text/javascript"></script>
    

      <link rel='permalink' href='/brightman/lbs/blob/e4c6408ed8425d8f6a315c523153025b9536a1f9/map_offset.py'>
    <meta property="og:title" content="lbs"/>
    <meta property="og:type" content="githubog:gitrepository"/>
    <meta property="og:url" content="https://github.com/brightman/lbs"/>
    <meta property="og:image" content="https://a248.e.akamai.net/assets.github.com/images/gravatars/gravatar-140.png?1329275960"/>
    <meta property="og:site_name" content="GitHub"/>
    <meta property="og:description" content="lbs - lib/tools"/>

    <meta name="description" content="lbs - lib/tools" />
  <link href="https://github.com/brightman/lbs/commits/master.atom" rel="alternate" title="Recent Commits to lbs:master" type="application/atom+xml" />

  </head>


  <body class="logged_out page-blob windows vis-public env-production " data-blob-contribs-enabled="yes">
    <div id="wrapper">

    
    
    

      <div id="header" class="true clearfix">
        <div class="container clearfix">
          <a class="site-logo" href="https://github.com">
            <!--[if IE]>
            <img alt="GitHub" class="github-logo" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7.png?1323882778" />
            <img alt="GitHub" class="github-logo-hover" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7-hover.png?1324325424" />
            <![endif]-->
            <img alt="GitHub" class="github-logo-4x" height="30" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7@4x.png?1323882778" />
            <img alt="GitHub" class="github-logo-4x-hover" height="30" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7@4x-hover.png?1324325424" />
          </a>

                  <!--
      make sure to use fully qualified URLs here since this nav
      is used on error pages on other domains
    -->
    <ul class="top-nav logged_out">
        <li class="pricing"><a href="https://github.com/plans">Signup and Pricing</a></li>
        <li class="explore"><a href="https://github.com/explore">Explore GitHub</a></li>
      <li class="features"><a href="https://github.com/features">Features</a></li>
        <li class="blog"><a href="https://github.com/blog">Blog</a></li>
      <li class="login"><a href="https://github.com/login?return_to=%2Fbrightman%2Flbs%2Fblob%2Fmaster%2Fmap_offset.py">Login</a></li>
    </ul>



          
        </div>
      </div>

      

            <div class="site" itemscope itemtype="http://schema.org/WebPage">
      <div class="container">
        <div class="pagehead repohead instapaper_ignore readability-menu">
        <div class="title-actions-bar">
          



              <ul class="pagehead-actions">


          <li><a href="/login?return_to=%2Fbrightman%2Flbs" class="minibutton btn-watch watch-button entice tooltipped leftwards" rel="nofollow" title="You must be logged in to use this feature"><span><span class="icon"></span>Watch</span></a></li>
          <li><a href="/login?return_to=%2Fbrightman%2Flbs" class="minibutton btn-fork fork-button entice tooltipped leftwards" rel="nofollow" title="You must be logged in to use this feature"><span><span class="icon"></span>Fork</span></a></li>


      <li class="repostats">
        <ul class="repo-stats">
          <li class="watchers ">
            <a href="/brightman/lbs/watchers" title="Watchers" class="tooltipped downwards">
              5
            </a>
          </li>
          <li class="forks">
            <a href="/brightman/lbs/network" title="Forks" class="tooltipped downwards">
              2
            </a>
          </li>
        </ul>
      </li>
    </ul>

          <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb">
            <span class="mini-icon public-repo"></span>
<a href="/brightman" itemprop="url">            <span itemprop="title">brightman</span>
            </a> /
            <strong><a href="/brightman/lbs" class="js-current-repository">lbs</a></strong>
          </h1>
        </div>

          

  <ul class="tabs">
    <li><a href="/brightman/lbs" class="selected" highlight="repo_sourcerepo_downloadsrepo_commitsrepo_tagsrepo_branches">Code</a></li>
    <li><a href="/brightman/lbs/network" highlight="repo_networkrepo_fork_queue">Network</a>
    <li><a href="/brightman/lbs/pulls" highlight="repo_pulls">Pull Requests <span class='counter'>0</span></a></li>

      <li><a href="/brightman/lbs/issues" highlight="repo_issues">Issues <span class='counter'>0</span></a></li>


    <li><a href="/brightman/lbs/graphs" highlight="repo_graphsrepo_contributors">Stats &amp; Graphs</a></li>

  </ul>

  
<div class="frame frame-center tree-finder" style="display:none"
      data-tree-list-url="/brightman/lbs/tree-list/e4c6408ed8425d8f6a315c523153025b9536a1f9"
      data-blob-url-prefix="/brightman/lbs/blob/e4c6408ed8425d8f6a315c523153025b9536a1f9"
    >

  <div class="breadcrumb">
    <span class="bold"><a href="/brightman/lbs">lbs</a></span> /
    <input class="tree-finder-input js-navigation-enable" type="text" name="query" autocomplete="off" spellcheck="false">
  </div>

    <div class="octotip">
      <p>
        <a href="/brightman/lbs/dismiss-tree-finder-help" class="dismiss js-dismiss-tree-list-help" title="Hide this notice forever" rel="nofollow">Dismiss</a>
        <span class="bold">Octotip:</span> You've activated the <em>file finder</em>
        by pressing <span class="kbd">t</span> Start typing to filter the
        file list. Use <span class="kbd badmono">↑</span> and
        <span class="kbd badmono">↓</span> to navigate,
        <span class="kbd">enter</span> to view files.
      </p>
    </div>

  <table class="tree-browser" cellpadding="0" cellspacing="0">
    <tr class="js-header"><th>&nbsp;</th><th>name</th></tr>
    <tr class="js-no-results no-results" style="display: none">
      <th colspan="2">No matching files</th>
    </tr>
    <tbody class="js-results-list js-navigation-container">
    </tbody>
  </table>
</div>

<div id="jump-to-line" style="display:none">
  <h2>Jump to Line</h2>
  <form accept-charset="UTF-8">
    <input name="utf8" type="hidden" value="&#x2713;" />
    <input class="textfield" type="text">
    <div class="full-button">
      <button type="submit" class="classy">
        <span>Go</span>
      </button>
    </div>
  </form>
</div>


<div class="subnav-bar">

  <ul class="actions subnav">
    <li><a href="/brightman/lbs/tags" class="blank" highlight="repo_tags">Tags <span class="counter">0</span></a></li>
    <li><a href="/brightman/lbs/downloads" class="blank downloads-blank" highlight="repo_downloads">Downloads <span class="counter">0</span></a></li>
    
  </ul>

  <ul class="scope">
    <li class="switcher">

      <div class="context-menu-container js-menu-container">
        <a href="#"
           class="minibutton bigger switcher js-menu-target js-commitish-button btn-branch repo-tree"
           data-master-branch="master"
           data-ref="master">
          <span><span class="icon"></span><i>branch:</i> master</span>
        </a>

        <div class="context-pane commitish-context js-menu-content">
          <a href="javascript:;" class="close js-menu-close"></a>
          <div class="context-title">Switch Branches/Tags</div>
          <div class="context-body pane-selector commitish-selector js-filterable-commitishes">
            <div class="filterbar">
              <div class="placeholder-field js-placeholder-field">
                <label class="placeholder" for="context-commitish-filter-field" data-placeholder-mode="sticky">Filter branches/tags</label>
                <input type="text" id="context-commitish-filter-field" class="commitish-filter" />
              </div>

              <ul class="tabs">
                <li><a href="#" data-filter="branches" class="selected">Branches</a></li>
                <li><a href="#" data-filter="tags">Tags</a></li>
              </ul>
            </div>

              <div class="commitish-item branch-commitish selector-item">
                <h4>
                    <a href="/brightman/lbs/blob/master/map_offset.py" data-name="master" rel="nofollow">master</a>
                </h4>
              </div>


            <div class="no-results" style="display:none">Nothing to show</div>
          </div>
        </div><!-- /.commitish-context-context -->
      </div>

    </li>
  </ul>

  <ul class="subnav with-scope">

    <li><a href="/brightman/lbs" class="selected" highlight="repo_source">Files</a></li>
    <li><a href="/brightman/lbs/commits/master" highlight="repo_commits">Commits</a></li>
    <li><a href="/brightman/lbs/branches" class="" highlight="repo_branches" rel="nofollow">Branches <span class="counter">1</span></a></li>
  </ul>

</div>

  
  
  


          

        </div><!-- /.repohead -->

        





<!-- block_view_fragment_key: views7/v8/blob:v19:531225d40d88498f88f92c073f490f88 -->
  <div id="slider">

    <div class="breadcrumb" data-path="map_offset.py/">
      <b itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/brightman/lbs/tree/e4c6408ed8425d8f6a315c523153025b9536a1f9" class="js-rewrite-sha" itemprop="url"><span itemprop="title">lbs</span></a></b> / <strong class="final-path">map_offset.py</strong> <span class="js-clippy clippy-button " data-clipboard-text="map_offset.py" data-copied-hint="copied!" data-copy-hint="copy to clipboard"></span>
    </div>


      <div class="commit file-history-tease" data-path="map_offset.py/">
        <img class="main-avatar" height="24" src="https://secure.gravatar.com/avatar/282527895166122fe049cb80a7b860ac?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png" width="24" />
        <span class="author"><a href="/brightman">brightman</a></span>
        <time class="js-relative-date" datetime="2011-04-10T03:06:18-07:00" title="2011-04-10 03:06:18">April 10, 2011</time>
        <div class="commit-title">
            <a href="/brightman/lbs/commit/608844ff24ea68a5727293dfcb8c1b30e5d7e4a1" class="message">	modified: map_offset.py</a>
        </div>

        <div class="participation">
          <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>1</strong> contributor</a></p>
          
        </div>
        <div id="blob_contributors_box" style="display:none">
          <h2>Users on GitHub who have contributed to this file</h2>
          <ul class="facebox-user-list">
            <li>
              <img height="24" src="https://secure.gravatar.com/avatar/282527895166122fe049cb80a7b860ac?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png" width="24" />
              <a href="/brightman">brightman</a>
            </li>
          </ul>
        </div>
      </div>

    <div class="frames">
      <div class="frame frame-center" data-path="map_offset.py/" data-permalink-url="/brightman/lbs/blob/e4c6408ed8425d8f6a315c523153025b9536a1f9/map_offset.py" data-title="lbs/map_offset.py at master · brightman/lbs · GitHub" data-type="blob">

        <div id="files" class="bubble">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><b class="mini-icon text-file"></b></span>
                <span class="mode" title="File Mode">100644</span>
                  <span>43 lines (37 sloc)</span>
                <span>1.175 kb</span>
              </div>
              <ul class="button-group actions">
                  <li>
                    <a class="grouped-button file-edit-link minibutton bigger lighter js-rewrite-sha" href="/brightman/lbs/edit/e4c6408ed8425d8f6a315c523153025b9536a1f9/map_offset.py" data-method="post" rel="nofollow"><span>Edit this file</span></a>
                  </li>

                <li>
                  <a href="/brightman/lbs/raw/master/map_offset.py" class="minibutton btn-raw grouped-button bigger lighter" id="raw-url"><span><span class="icon"></span>Raw</span></a>
                </li>
                  <li>
                    <a href="/brightman/lbs/blame/master/map_offset.py" class="minibutton btn-blame grouped-button bigger lighter"><span><span class="icon"></span>Blame</span></a>
                  </li>
                <li>
                  <a href="/brightman/lbs/commits/master/map_offset.py" class="minibutton btn-history grouped-button bigger lighter" rel="nofollow"><span><span class="icon"></span>History</span></a>
                </li>
              </ul>
            </div>
              <div class="data type-python">
      <table cellpadding="0" cellspacing="0" class="lines">
        <tr>
          <td>
            <pre class="line_numbers"><span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
</pre>
          </td>
          <td width="100%">
                <div class="highlight"><pre><div class='line' id='LC1'><span class="c">#!/usr/bin/env python</span></div><div class='line' id='LC2'><span class="c">#coding=utf-8</span></div><div class='line' id='LC3'><span class="kn">import</span> <span class="nn">pdb</span><span class="o">,</span><span class="nn">pickle</span><span class="o">,</span><span class="nn">math</span></div><div class='line' id='LC4'><span class="sd">&#39;&#39;&#39;</span></div><div class='line' id='LC5'><span class="sd">offset={}</span></div><div class='line' id='LC6'><span class="sd">f=open(&#39;offset_min1.txt&#39;)</span></div><div class='line' id='LC7'><span class="sd">for l in f.readlines():</span></div><div class='line' id='LC8'><span class="sd">	p = l.strip(&#39;\n&#39;).split(&#39;,&#39;)</span></div><div class='line' id='LC9'><span class="sd">	offset[(float(p[0].strip(&#39;&quot;&#39;)),float(p[1].strip(&#39;&quot;&#39;)))]=(float(p[4].strip(&#39;&quot;&#39;)),float(p[5].strip(&#39;&quot;&#39;)))</span></div><div class='line' id='LC10'><span class="sd">pickle.dump(offset,f1)</span></div><div class='line' id='LC11'><span class="sd">f.close()</span></div><div class='line' id='LC12'><span class="sd">&#39;&#39;&#39;</span></div><div class='line' id='LC13'><span class="n">f1</span><span class="o">=</span><span class="nb">open</span><span class="p">(</span><span class="s">&#39;gps2gmap.offset&#39;</span><span class="p">,</span><span class="s">&#39;r&#39;</span><span class="p">)</span></div><div class='line' id='LC14'><span class="n">offset</span> <span class="o">=</span> <span class="n">pickle</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">f1</span><span class="p">)</span></div><div class='line' id='LC15'><span class="n">f1</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC16'><br/></div><div class='line' id='LC17'><span class="k">def</span> <span class="nf">gps2gmap</span><span class="p">(</span><span class="n">lat</span><span class="p">,</span><span class="n">lng</span><span class="p">):</span></div><div class='line' id='LC18'>	<span class="n">base_lat</span><span class="p">,</span><span class="n">base_lng</span> <span class="o">=</span> <span class="nb">float</span><span class="p">(</span><span class="s">&quot;</span><span class="si">%.1f</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">lat</span><span class="p">),</span><span class="nb">float</span><span class="p">(</span><span class="s">&quot;</span><span class="si">%.1f</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">lng</span><span class="p">)</span></div><div class='line' id='LC19'>	<span class="k">if</span> <span class="n">offset</span><span class="o">.</span><span class="n">get</span><span class="p">((</span><span class="n">base_lng</span><span class="p">,</span><span class="n">base_lat</span><span class="p">)):</span></div><div class='line' id='LC20'>		<span class="n">offset_lng</span><span class="p">,</span><span class="n">offset_lat</span> <span class="o">=</span> <span class="n">offset</span><span class="o">.</span><span class="n">get</span><span class="p">((</span><span class="n">base_lng</span><span class="p">,</span><span class="n">base_lat</span><span class="p">))</span></div><div class='line' id='LC21'>		<span class="n">new_lng</span><span class="p">,</span><span class="n">new_lat</span> <span class="o">=</span> <span class="n">lng</span> <span class="o">+</span> <span class="n">offset_lng</span><span class="p">,</span><span class="n">lat</span> <span class="o">+</span> <span class="n">offset_lat</span></div><div class='line' id='LC22'>		<span class="k">return</span> <span class="p">(</span><span class="n">new_lat</span><span class="p">,</span><span class="n">new_lng</span><span class="p">)</span></div><div class='line' id='LC23'>	<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC24'>		<span class="k">return</span> <span class="n">lat</span><span class="p">,</span><span class="n">lng</span></div><div class='line' id='LC25'><br/></div><div class='line' id='LC26'><span class="k">def</span> <span class="nf">gps2bmap</span><span class="p">(</span><span class="n">lat</span><span class="p">,</span><span class="n">lng</span><span class="p">):</span></div><div class='line' id='LC27'>	<span class="k">pass</span></div><div class='line' id='LC28'><br/></div><div class='line' id='LC29'><span class="k">def</span> <span class="nf">gps2sgmap</span><span class="p">(</span><span class="n">lat</span><span class="p">,</span><span class="n">lng</span><span class="p">):</span></div><div class='line' id='LC30'>	<span class="k">pass</span></div><div class='line' id='LC31'><br/></div><div class='line' id='LC32'><span class="k">def</span> <span class="nf">latlng_dis</span><span class="p">(</span><span class="n">lat1</span><span class="p">,</span><span class="n">lng1</span><span class="p">,</span><span class="n">lat2</span><span class="p">,</span><span class="n">lng2</span><span class="p">):</span></div><div class='line' id='LC33'>	<span class="n">radlat1</span><span class="p">,</span><span class="n">radlat2</span><span class="p">,</span><span class="n">radlng1</span><span class="p">,</span><span class="n">radlng2</span> <span class="o">=</span> <span class="n">lat1</span> <span class="o">*</span> <span class="n">math</span><span class="o">.</span><span class="n">pi</span><span class="o">/</span><span class="mf">180.0</span><span class="p">,</span><span class="n">lat2</span> <span class="o">*</span> <span class="n">math</span><span class="o">.</span><span class="n">pi</span><span class="o">/</span><span class="mf">180.0</span><span class="p">,</span><span class="n">lng1</span> <span class="o">*</span> <span class="n">math</span><span class="o">.</span><span class="n">pi</span><span class="o">/</span><span class="mf">180.0</span><span class="p">,</span><span class="n">lng2</span> <span class="o">*</span> <span class="n">math</span><span class="o">.</span><span class="n">pi</span><span class="o">/</span><span class="mf">180.0</span></div><div class='line' id='LC34'>	<span class="n">a</span> <span class="o">=</span> <span class="n">radlat1</span> <span class="o">-</span> <span class="n">radlat2</span></div><div class='line' id='LC35'>	<span class="n">b</span> <span class="o">=</span> <span class="n">radlng1</span> <span class="o">-</span> <span class="n">radlng2</span></div><div class='line' id='LC36'>	<span class="n">s</span> <span class="o">=</span> <span class="mi">2</span> <span class="o">*</span> <span class="n">math</span><span class="o">.</span><span class="n">asin</span><span class="p">(</span><span class="n">math</span><span class="o">.</span><span class="n">sqrt</span><span class="p">(</span><span class="n">math</span><span class="o">.</span><span class="n">pow</span><span class="p">(</span><span class="n">math</span><span class="o">.</span><span class="n">sin</span><span class="p">(</span><span class="n">a</span><span class="o">/</span><span class="mi">2</span><span class="p">),</span><span class="mi">2</span><span class="p">)</span><span class="o">+</span><span class="n">math</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="n">radlat1</span><span class="p">)</span><span class="o">*</span><span class="n">math</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="n">radlat2</span><span class="p">)</span> <span class="o">*</span><span class="n">math</span><span class="o">.</span><span class="n">pow</span><span class="p">(</span><span class="n">math</span><span class="o">.</span><span class="n">sin</span><span class="p">(</span><span class="n">b</span><span class="o">/</span><span class="mi">2</span><span class="p">),</span><span class="mi">2</span><span class="p">)))</span></div><div class='line' id='LC37'>	<span class="n">s</span> <span class="o">*=</span> <span class="mf">6378.137</span></div><div class='line' id='LC38'>	<span class="n">s</span> <span class="o">*=</span> <span class="mi">1000</span></div><div class='line' id='LC39'>	<span class="k">return</span> <span class="n">s</span></div><div class='line' id='LC40'><br/></div><div class='line' id='LC41'><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&quot;__main__&quot;</span><span class="p">:</span></div><div class='line' id='LC42'>	<span class="k">print</span> <span class="n">gps2gmap</span><span class="p">(</span><span class="mf">39.902869</span><span class="p">,</span><span class="mf">116.223233</span><span class="p">)</span></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

          </div>
        </div>
      </div>
    </div>

  </div>

<div class="frame frame-loading large-loading-area" style="display:none;" data-tree-list-url="/brightman/lbs/tree-list/e4c6408ed8425d8f6a315c523153025b9536a1f9" data-blob-url-prefix="/brightman/lbs/blob/e4c6408ed8425d8f6a315c523153025b9536a1f9">
  <img src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-64.gif?1329872008" height="64" width="64">
</div>

      </div>
      <div class="context-overlay"></div>
    </div>

      <div id="footer-push"></div><!-- hack for sticky footer -->
    </div><!-- end of wrapper - hack for sticky footer -->

      <!-- footer -->
      <div id="footer" >
        
  <div class="upper_footer">
     <div class="container clearfix">

       <!--[if IE]><h4 id="blacktocat_ie">GitHub Links</h4><![endif]-->
       <![if !IE]><h4 id="blacktocat">GitHub Links</h4><![endif]>

       <ul class="footer_nav">
         <h4>GitHub</h4>
         <li><a href="https://github.com/about">About</a></li>
         <li><a href="https://github.com/blog">Blog</a></li>
         <li><a href="https://github.com/features">Features</a></li>
         <li><a href="https://github.com/contact">Contact &amp; Support</a></li>
         <li><a href="https://github.com/training">Training</a></li>
         <li><a href="http://enterprise.github.com/">GitHub Enterprise</a></li>
         <li><a href="http://status.github.com/">Site Status</a></li>
       </ul>

       <ul class="footer_nav">
         <h4>Tools</h4>
         <li><a href="http://get.gaug.es/">Gauges: Analyze web traffic</a></li>
         <li><a href="http://speakerdeck.com">Speaker Deck: Presentations</a></li>
         <li><a href="https://gist.github.com">Gist: Code snippets</a></li>
         <li><a href="http://mac.github.com/">GitHub for Mac</a></li>
         <li><a href="http://mobile.github.com/">Issues for iPhone</a></li>
         <li><a href="http://jobs.github.com/">Job Board</a></li>
       </ul>

       <ul class="footer_nav">
         <h4>Extras</h4>
         <li><a href="http://shop.github.com/">GitHub Shop</a></li>
         <li><a href="http://octodex.github.com/">The Octodex</a></li>
       </ul>

       <ul class="footer_nav">
         <h4>Documentation</h4>
         <li><a href="http://help.github.com/">GitHub Help</a></li>
         <li><a href="http://developer.github.com/">Developer API</a></li>
         <li><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></li>
         <li><a href="http://pages.github.com/">GitHub Pages</a></li>
       </ul>

     </div><!-- /.site -->
  </div><!-- /.upper_footer -->

<div class="lower_footer">
  <div class="container clearfix">
    <!--[if IE]><div id="legal_ie"><![endif]-->
    <![if !IE]><div id="legal"><![endif]>
      <ul>
          <li><a href="https://github.com/site/terms">Terms of Service</a></li>
          <li><a href="https://github.com/site/privacy">Privacy</a></li>
          <li><a href="https://github.com/security">Security</a></li>
      </ul>

      <p>&copy; 2012 <span title="0.05958s from fe6.rs.github.com">GitHub</span> Inc. All rights reserved.</p>
    </div><!-- /#legal or /#legal_ie-->

      <div class="sponsor">
        <a href="http://www.rackspace.com" class="logo">
          <img alt="Dedicated Server" height="36" src="https://a248.e.akamai.net/assets.github.com/images/modules/footer/rackspaces_logo.png?1329521041" width="38" />
        </a>
        Powered by the <a href="http://www.rackspace.com ">Dedicated
        Servers</a> and<br/> <a href="http://www.rackspacecloud.com">Cloud
        Computing</a> of Rackspace Hosting<span>&reg;</span>
      </div>
  </div><!-- /.site -->
</div><!-- /.lower_footer -->

      </div><!-- /#footer -->

    

<div id="keyboard_shortcuts_pane" class="instapaper_ignore readability-extra" style="display:none">
  <h2>Keyboard Shortcuts <small><a href="#" class="js-see-all-keyboard-shortcuts">(see all)</a></small></h2>

  <div class="columns threecols">
    <div class="column first">
      <h3>Site wide shortcuts</h3>
      <dl class="keyboard-mappings">
        <dt>s</dt>
        <dd>Focus site search</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>?</dt>
        <dd>Bring up this help dialog</dd>
      </dl>
    </div><!-- /.column.first -->

    <div class="column middle" style='display:none'>
      <h3>Commit list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selection down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selection up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>c <em>or</em> o <em>or</em> enter</dt>
        <dd>Open commit</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>y</dt>
        <dd>Expand URL to its canonical form</dd>
      </dl>
    </div><!-- /.column.first -->

    <div class="column last" style='display:none'>
      <h3>Pull request list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selection down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selection up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>o <em>or</em> enter</dt>
        <dd>Open issue</dd>
      </dl>
    </div><!-- /.columns.last -->

  </div><!-- /.columns.equacols -->

  <div style='display:none'>
    <div class="rule"></div>

    <h3>Issues</h3>

    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>j</dt>
          <dd>Move selection down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>k</dt>
          <dd>Move selection up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>x</dt>
          <dd>Toggle selection</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o <em>or</em> enter</dt>
          <dd>Open issue</dd>
        </dl>
      </div><!-- /.column.first -->
      <div class="column middle">
        <dl class="keyboard-mappings">
          <dt>I</dt>
          <dd>Mark selection as read</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>U</dt>
          <dd>Mark selection as unread</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>y</dt>
          <dd>Remove selection from view</dd>
        </dl>
      </div><!-- /.column.middle -->
      <div class="column last">
        <dl class="keyboard-mappings">
          <dt>c</dt>
          <dd>Create issue</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>l</dt>
          <dd>Create label</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>i</dt>
          <dd>Back to inbox</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>u</dt>
          <dd>Back to issues</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>/</dt>
          <dd>Focus issues search</dd>
        </dl>
      </div>
    </div>
  </div>

  <div style='display:none'>
    <div class="rule"></div>

    <h3>Issues Dashboard</h3>

    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>j</dt>
          <dd>Move selection down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>k</dt>
          <dd>Move selection up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o <em>or</em> enter</dt>
          <dd>Open issue</dd>
        </dl>
      </div><!-- /.column.first -->
    </div>
  </div>

  <div style='display:none'>
    <div class="rule"></div>

    <h3>Network Graph</h3>
    <div class="columns equacols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt><span class="badmono">←</span> <em>or</em> h</dt>
          <dd>Scroll left</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">→</span> <em>or</em> l</dt>
          <dd>Scroll right</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">↑</span> <em>or</em> k</dt>
          <dd>Scroll up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">↓</span> <em>or</em> j</dt>
          <dd>Scroll down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>t</dt>
          <dd>Toggle visibility of head labels</dd>
        </dl>
      </div><!-- /.column.first -->
      <div class="column last">
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">←</span> <em>or</em> shift h</dt>
          <dd>Scroll all the way left</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">→</span> <em>or</em> shift l</dt>
          <dd>Scroll all the way right</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">↑</span> <em>or</em> shift k</dt>
          <dd>Scroll all the way up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">↓</span> <em>or</em> shift j</dt>
          <dd>Scroll all the way down</dd>
        </dl>
      </div><!-- /.column.last -->
    </div>
  </div>

  <div >
    <div class="rule"></div>
    <div class="columns threecols">
      <div class="column first" >
        <h3>Source Code Browsing</h3>
        <dl class="keyboard-mappings">
          <dt>t</dt>
          <dd>Activates the file finder</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>l</dt>
          <dd>Jump to line</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>w</dt>
          <dd>Switch branch/tag</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>y</dt>
          <dd>Expand URL to its canonical form</dd>
        </dl>
      </div>
    </div>
  </div>
</div>

    <div id="markdown-help" class="instapaper_ignore readability-extra">
  <h2>Markdown Cheat Sheet</h2>

  <div class="cheatsheet-content">

  <div class="mod">
    <div class="col">
      <h3>Format Text</h3>
      <p>Headers</p>
      <pre>
# This is an &lt;h1&gt; tag
## This is an &lt;h2&gt; tag
###### This is an &lt;h6&gt; tag</pre>
     <p>Text styles</p>
     <pre>
*This text will be italic*
_This will also be italic_
**This text will be bold**
__This will also be bold__

*You **can** combine them*
</pre>
    </div>
    <div class="col">
      <h3>Lists</h3>
      <p>Unordered</p>
      <pre>
* Item 1
* Item 2
  * Item 2a
  * Item 2b</pre>
     <p>Ordered</p>
     <pre>
1. Item 1
2. Item 2
3. Item 3
   * Item 3a
   * Item 3b</pre>
    </div>
    <div class="col">
      <h3>Miscellaneous</h3>
      <p>Images</p>
      <pre>
![GitHub Logo](/images/logo.png)
Format: ![Alt Text](url)
</pre>
     <p>Links</p>
     <pre>
http://github.com - automatic!
[GitHub](http://github.com)</pre>
<p>Blockquotes</p>
     <pre>
As Kanye West said:

> We're living the future so
> the present is our past.
</pre>
    </div>
  </div>
  <div class="rule"></div>

  <h3>Code Examples in Markdown</h3>
  <div class="col">
      <p>Syntax highlighting with <a href="http://github.github.com/github-flavored-markdown/" title="GitHub Flavored Markdown" target="_blank">GFM</a></p>
      <pre>
```javascript
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```</pre>
    </div>
    <div class="col">
      <p>Or, indent your code 4 spaces</p>
      <pre>
Here is a Python code example
without syntax highlighting:

    def foo:
      if not bar:
        return true</pre>
    </div>
    <div class="col">
      <p>Inline code for comments</p>
      <pre>
I think you should use an
`&lt;addr&gt;` element here instead.</pre>
    </div>
  </div>

  </div>
</div>


    <div class="ajax-error-message">
      <p><span class="icon"></span> Something went wrong with that request. Please try again. <a href="javascript:;" class="ajax-error-dismiss">Dismiss</a></p>
    </div>

    <div id="logo-popup">
      <h2>Looking for the GitHub logo?</h2>
      <ul>
        <li>
          <h4>GitHub Logo</h4>
          <a href="http://github-media-downloads.s3.amazonaws.com/GitHub_Logos.zip"><img alt="Github_logo" src="https://a248.e.akamai.net/assets.github.com/images/modules/about_page/github_logo.png?1306884371" /></a>
          <a href="http://github-media-downloads.s3.amazonaws.com/GitHub_Logos.zip" class="minibutton btn-download download"><span><span class="icon"></span>Download</span></a>
        </li>
        <li>
          <h4>The Octocat</h4>
          <a href="http://github-media-downloads.s3.amazonaws.com/Octocats.zip"><img alt="Octocat" src="https://a248.e.akamai.net/assets.github.com/images/modules/about_page/octocat.png?1306884371" /></a>
          <a href="http://github-media-downloads.s3.amazonaws.com/Octocats.zip" class="minibutton btn-download download"><span><span class="icon"></span>Download</span></a>
        </li>
      </ul>
    </div>

    
    
    
    <span id='server_response_time' data-time='0.06128' data-host='fe6'></span>
  </body>
</html>

