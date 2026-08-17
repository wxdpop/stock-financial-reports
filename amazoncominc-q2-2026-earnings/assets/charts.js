/**
 * Amazon Q2 2026 ECharts Charts
 */
(function () {
  'use strict';
  var rootStyle = getComputedStyle(document.documentElement);
  function cssVar(name, fallback) {
    var v = rootStyle.getPropertyValue(name);
    v = v ? v.trim() : '';
    return v || fallback;
  }
  var P = {
    primary:    cssVar('--accent',         '#0071e3'),
    accent:     cssVar('--accent',         '#0071e3'),
    positive:   cssVar('--accent2',        '#34c759'),
    negative:   cssVar('--neg',            '#d93025'),
    neutral:    cssVar('--muted',          '#6e6e73'),
    text:       cssVar('--ink',            '#1d1d1f'),
    textMuted:  cssVar('--muted',          '#6e6e73'),
    grid:       cssVar('--rule',           '#d2d2d7'),
    surface:    cssVar('--bg2',            '#ffffff'),
    s1: '#0071e3', s2: '#34c759', s3: '#ff9500', s4: '#af52de', s5: '#ff3b30'
  };
  var isMobile = window.innerWidth <= 700;
  function fs(b) { return isMobile ? Math.round(b * 0.86) : b; }
  function makeGrid() {
    return isMobile
      ? { left: 38, right: 16, top: 34, bottom: 58, containLabel: true }
      : { left: 56, right: 28, top: 42, bottom: 48, containLabel: true };
  }
  function axisLabel() { return { color: P.textMuted, fontSize: fs(12) }; }
  function makeChart(el) { return echarts.init(el, null, { renderer: 'svg' }); }
  function render(el, option) {
    if (!el) return null;
    var chart = makeChart(el);
    chart.setOption(option);
    window.addEventListener('resize', function () { chart.resize(); });
    return chart;
  }

  /* 1. chart-revenue-trend */
  (function () {
    var el = document.getElementById('chart-revenue-trend');
    if (!el) return;
    var cats = ['24Q3','24Q4','25Q1','25Q2','25Q3','25Q4','26Q1','26Q2'];
    var revenue = [1589, 1878, 1557, 1677, 1802, 2134, 1815, 2006];
    var netIncome = [153, 200, 171, 182, 212, 212, 303, 626];
    var option = {
      animation: false, color: [P.s1, P.s2], grid: makeGrid(),
      legend: { top: 0, textStyle: { color: P.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: { trigger: 'axis' },
      xAxis: { type: 'category', data: cats, axisLabel: Object.assign({}, axisLabel(), { rotate: isMobile ? 45 : 0 }), axisLine: { lineStyle: { color: P.grid } }, axisTick: { show: false } },
      yAxis: [
        { type: 'value', name: '营收(亿美元)', nameTextStyle: { color: P.textMuted, fontSize: fs(11) }, axisLabel: axisLabel(), splitLine: { lineStyle: { color: P.grid } } },
        { type: 'value', name: '净利润(亿美元)', nameTextStyle: { color: P.textMuted, fontSize: fs(11) }, axisLabel: axisLabel(), splitLine: { show: false } }
      ],
      series: [
        { name: '营收', type: 'bar', yAxisIndex: 0, data: revenue, barMaxWidth: isMobile ? 18 : 30, itemStyle: { color: P.s1, borderRadius: [3,3,0,0] } },
        { name: '净利润', type: 'line', yAxisIndex: 1, data: netIncome, smooth: true, symbol: 'circle', symbolSize: isMobile ? 6 : 8, lineStyle: { width: 2, color: P.s2 }, itemStyle: { color: P.s2 } }
      ]
    };
    render(el, option);
  })();

  /* 2. chart-revenue-mix */
  (function () {
    var el = document.getElementById('chart-revenue-mix');
    if (!el) return;
    var data = [
      { name: '在线零售', value: 704 }, { name: '三方卖家', value: 420 },
      { name: 'AWS', value: 422 }, { name: '广告', value: 198 },
      { name: '订阅', value: 116 }, { name: '实体零售', value: 56 }, { name: '其他', value: 90 }
    ];
    var colors = [P.s1, '#5ac8fa', P.s4, P.s3, P.s2, P.s5, P.neutral];
    var lg = isMobile ? { bottom: 0, left: 'center', orient: 'horizontal', textStyle: { color: P.textMuted, fontSize: fs(11) }, itemWidth: fs(10), itemHeight: fs(10) }
      : { top: 'middle', right: 8, orient: 'vertical', textStyle: { color: P.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) };
    var option = {
      animation: false, color: colors, legend: lg,
      tooltip: { trigger: 'item', formatter: '{b}: ${c}亿 ({d}%)' },
      series: [{ type: 'pie', radius: isMobile ? ['38%','62%'] : ['52%','72%'], center: isMobile ? ['50%','42%'] : ['38%','50%'],
        avoidLabelOverlap: true, itemStyle: { borderColor: P.surface, borderWidth: 2 },
        label: { show: !isMobile, color: P.text, fontSize: fs(12), formatter: '{d}%' }, labelLine: { show: !isMobile }, data: data }]
    };
    render(el, option);
  })();

  /* 3. chart-margin-trend */
  (function () {
    var el = document.getElementById('chart-margin-trend');
    if (!el) return;
    var cats = ['24Q3','24Q4','25Q1','25Q2','25Q3','25Q4','26Q1','26Q2'];
    var gm = [49.2, 47.3, 50.6, 51.8, 50.8, 48.5, 51.8, 51.3];
    var om = [9.6, 11.3, 11.8, 11.4, 9.7, 11.7, 13.1, 13.7];
    var nm = [9.6, 10.7, 11.0, 10.8, 11.8, 9.9, 16.7, 31.2];
    var option = {
      animation: false, color: [P.s1, P.s2, P.s3], grid: makeGrid(),
      legend: { top: 0, textStyle: { color: P.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: { trigger: 'axis', formatter: function(p) { return p.map(function(x){ return x.marker + x.seriesName + ': ' + x.value + '%'; }).join('<br/>'); } },
      xAxis: { type: 'category', data: cats, axisLabel: Object.assign({}, axisLabel(), { rotate: isMobile ? 45 : 0 }), axisLine: { lineStyle: { color: P.grid } }, axisTick: { show: false } },
      yAxis: { type: 'value', name: '%', nameTextStyle: { color: P.textMuted, fontSize: fs(11) }, axisLabel: axisLabel(), splitLine: { lineStyle: { color: P.grid } } },
      series: [
        { name: '毛利率', type: 'line', data: gm, smooth: true, symbol: 'circle', symbolSize: fs(7), lineStyle: { width: 2.5 }, itemStyle: { color: P.s1 } },
        { name: '营业利润率', type: 'line', data: om, smooth: true, symbol: 'diamond', symbolSize: fs(7), lineStyle: { width: 2.5 }, itemStyle: { color: P.s2 } },
        { name: '净利率', type: 'line', data: nm, smooth: true, symbol: 'triangle', symbolSize: fs(8), lineStyle: { width: 2.5, type: 'dashed' }, itemStyle: { color: P.s3 } }
      ]
    };
    render(el, option);
  })();

  /* 4. chart-cashflow */
  (function () {
    var el = document.getElementById('chart-cashflow');
    if (!el) return;
    var cats = ['25Q3','25Q4','26Q1','26Q2'];
    var ocf = [320, 380, 427, 466];
    var capex = [280, 350, 430, 542];
    var fcf = [40, 30, -3, -76];
    var option = {
      animation: false, color: [P.s2, P.s5, P.s1], grid: makeGrid(),
      legend: { top: 0, textStyle: { color: P.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
      xAxis: { type: 'category', data: cats, axisLabel: Object.assign({}, axisLabel()), axisLine: { lineStyle: { color: P.grid } }, axisTick: { show: false } },
      yAxis: { type: 'value', name: '亿美元', nameTextStyle: { color: P.textMuted, fontSize: fs(11) }, axisLabel: axisLabel(), splitLine: { lineStyle: { color: P.grid } } },
      series: [
        { name: '经营现金流', type: 'bar', data: ocf, barMaxWidth: isMobile ? 16 : 28, itemStyle: { color: P.s2, borderRadius: [3,3,0,0] } },
        { name: '资本支出', type: 'bar', data: capex.map(function(v){ return -v; }), barMaxWidth: isMobile ? 16 : 28, itemStyle: { color: P.s5, borderRadius: [3,3,0,0] } },
        { name: '自由现金流', type: 'line', data: fcf, smooth: true, symbol: 'circle', symbolSize: fs(8), lineStyle: { width: 2.5, color: P.s1 }, itemStyle: { color: P.s1 } }
      ]
    };
    render(el, option);
  })();

  /* 5. chart-kpi-trend */
  (function () {
    var el = document.getElementById('chart-kpi-trend');
    if (!el) return;
    var cats = ['24Q3','24Q4','25Q1','25Q2','25Q3','25Q4','26Q1','26Q2'];
    var awsGrowth = [19.1, 18.8, 18.5, 18.7, 19.8, 20.5, 25.0, 36.7];
    var adGrowth = [24.0, 24.5, 25.0, 25.5, 26.0, 26.2, 26.5, 26.0];
    var option = {
      animation: false, color: [P.s4, P.s3], grid: makeGrid(),
      legend: { top: 0, textStyle: { color: P.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: { trigger: 'axis', formatter: function(p) { return p.map(function(x){ return x.marker + x.seriesName + ': ' + x.value + '%'; }).join('<br/>'); } },
      xAxis: { type: 'category', data: cats, axisLabel: Object.assign({}, axisLabel(), { rotate: isMobile ? 45 : 0 }), axisLine: { lineStyle: { color: P.grid } }, axisTick: { show: false } },
      yAxis: { type: 'value', name: '同比增速(%)', nameTextStyle: { color: P.textMuted, fontSize: fs(11) }, axisLabel: axisLabel(), splitLine: { lineStyle: { color: P.grid } } },
      series: [
        { name: 'AWS增速', type: 'line', data: awsGrowth, smooth: true, symbol: 'circle', symbolSize: fs(8), lineStyle: { width: 3 }, itemStyle: { color: P.s4 }, areaStyle: { color: 'rgba(175,82,222,0.1)' } },
        { name: '广告增速', type: 'line', data: adGrowth, smooth: true, symbol: 'diamond', symbolSize: fs(7), lineStyle: { width: 2.5 }, itemStyle: { color: P.s3 } }
      ]
    };
    render(el, option);
  })();

  /* 6. chart-geo */
  (function () {
    var el = document.getElementById('chart-geo');
    if (!el) return;
    var data = [{ name: '北美', value: 1161 }, { name: '国际', value: 423 }, { name: 'AWS(全球)', value: 422 }];
    var colors = [P.s1, P.s2, P.s4];
    var lg = isMobile ? { bottom: 0, left: 'center', orient: 'horizontal', textStyle: { color: P.textMuted, fontSize: fs(11) }, itemWidth: fs(10), itemHeight: fs(10) }
      : { top: 'middle', right: 8, orient: 'vertical', textStyle: { color: P.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) };
    var option = {
      animation: false, color: colors, legend: lg,
      tooltip: { trigger: 'item', formatter: '{b}: ${c}亿 ({d}%)' },
      series: [{ type: 'pie', radius: isMobile ? ['38%','62%'] : ['52%','72%'], center: isMobile ? ['50%','42%'] : ['38%','50%'],
        avoidLabelOverlap: true, itemStyle: { borderColor: P.surface, borderWidth: 2 },
        label: { show: !isMobile, color: P.text, fontSize: fs(12), formatter: '{b}
{d}%' }, labelLine: { show: !isMobile }, data: data }]
    };
    render(el, option);
  })();

  /* 7. chart-radar */
  (function () {
    var el = document.getElementById('chart-radar');
    if (!el) return;
    var indicator = [
      { name: '营收增速', max: 40 }, { name: 'AWS增速', max: 40 },
      { name: '毛利率', max: 60 }, { name: '营业利润率', max: 20 },
      { name: '净利率', max: 35 }, { name: '现金储备(十亿)', max: 120 }
    ];
    var value = [20, 37, 51.3, 13.7, 31.2, 101.8];
    var option = {
      animation: false, color: [P.s1],
      legend: { top: 0, textStyle: { color: P.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: {},
      radar: {
        indicator: indicator, shape: 'polygon', splitNumber: 4,
        axisName: { color: P.textMuted, fontSize: fs(11) },
        splitArea: { areaStyle: { color: ['rgba(0,113,227,0.02)','rgba(0,113,227,0.04)','rgba(0,113,227,0.02)','rgba(0,113,227,0.04)'] } },
        splitLine: { lineStyle: { color: P.grid } }, axisLine: { lineStyle: { color: P.grid } }
      },
      series: [{ type: 'radar', data: [{ value: value, name: 'Q2 2026', areaStyle: { color: 'rgba(0,113,227,0.2)' }, lineStyle: { color: P.s1, width: 2 }, itemStyle: { color: P.s1 } }], symbol: 'circle', symbolSize: fs(6) }]
    };
    render(el, option);
  })();

})();
