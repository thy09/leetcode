#dict version
begin = 0
int_begin = 1
frac_begin = 2
exp_begin = 3
inte = 4
frac = 5
exp = 6
end = 7
exp_ready = 8
byebye = 9

count = 10

fsm = {'.':[[set([inte]),frac],
            [set([int_begin]),frac_begin],
            [set([begin]),frac_begin]],
       '-+':[[set([begin]),int_begin],
             [set([exp_begin]),exp_ready]
             ],
       'eE':[[set([inte,frac]),exp_begin]],
       '0123456789':[[set([begin,int_begin,inte]),inte],
                     [set([frac,frac_begin]),frac],
                     [set([exp_begin,exp_ready,exp]),exp]],
       ' ':[[set([begin]),begin],
            [set([inte,frac,exp,end]),end],
            ],
       }
fsm_dict = {}
for key,mappings in fsm.iteritems():
    iomap = [9] * count
    for inps,outp in mappings:
        for inp in inps:
            iomap[inp] = outp
    for k in key:
        fsm_dict[k] = iomap

class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        status = begin
        for c in s:
            iomap = fsm_dict.get(c)
            if iomap:
            	status = iomap[status]
            	if status == byebye:
            		return False
            else:
            	return False
        return True if status in set([frac,inte,exp,end]) else False

nums = ['-1.2','-a','.',' .3']
s = Solution()
for num in nums:
	print s.isNumber(num),num
