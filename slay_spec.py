from mamba import description,context,it
from expects import expect,equal

import slay

with description('Slay') as self:
    with context('when a list is passed to the ch_dup method, in the user mode'):
        with it('will check for possible duplicates in the list'):
            sample_list = [1,2,3,1,4]
            sla = slay.Slay(sample_list)
            expect(sla.ch_dup(sample_list,"uf")).to(equal(True))

        with it('will check for possible duplicates in the list'):
            sample_list = []
            sla = slay.Slay(sample_list)
            expect(sla.ch_dup(sample_list,"uf")).to(equal("Empty List"))

        with it('will check for possible duplicates in the list'):
            sample_list = [1,2,3]
            sla = slay.Slay(sample_list)
            expect(sla.ch_dup(sample_list,"uf")).to(equal(False))
        
        with it('will check for possible duplicates in the list'):
            sample_list = [1]
            sla = slay.Slay(sample_list)
            expect(sla.ch_dup(sample_list,"uf")).to(equal(False))

with description('Slay') as self:
    with context('when a list is passed to the ch_dup method, in the user mode'):
        with it('will check for possible duplicates in the list'):
            sample_list = [1,2,3,1,4]
            sla = slay.Slay(sample_list)
            expect(sla.ch_dup(sample_list,"uw")).to(equal(True))

        with it('will check for possible duplicates in the list'):
            sample_list = []
            sla = slay.Slay(sample_list)
            expect(sla.ch_dup(sample_list,"uw")).to(equal("Empty List"))

        with it('will check for possible duplicates in the list'):
            sample_list = [1,2,3]
            sla = slay.Slay(sample_list)
            expect(sla.ch_dup(sample_list,"uw")).to(equal(False))
        
        with it('will check for possible duplicates in the list'):
            sample_list = [1]
            sla = slay.Slay(sample_list)
            expect(sla.ch_dup(sample_list,"uw")).to(equal(False))

with description('Slay') as self:
    with context('when a list is passed to the ch_dup method, in the system mode'):
        with it('will check for possible duplicates in the list'):
            sample_list = [1,2,3,1,4]
            sla = slay.Slay(sample_list)
            expect(sla.ch_dup(sample_list,"s")).to(equal(True))

        with it('will check for possible duplicates in the list'):
            sample_list = []
            sla = slay.Slay(sample_list)
            expect(sla.ch_dup(sample_list,"s")).to(equal("Empty List"))

        with it('will check for possible duplicates in the list'):
            sample_list = [1,2,3]
            sla = slay.Slay(sample_list)
            expect(sla.ch_dup(sample_list,"s")).to(equal(False))
        
        with it('will check for possible duplicates in the list'):
            sample_list = [1]
            sla = slay.Slay(sample_list)
            expect(sla.ch_dup(sample_list,"s")).to(equal(False))

with description('Slay') as self:
    with context('when a list is passed to the ch_dup method'):
        with it('and no mode is specified, will throw an error'):
            sample_list = [1,2,3,1,4]
            sla = slay.Slay(sample_list)
            expect(sla.ch_dup(sample_list,"")).to(equal("Invalid Mode"))

        with it('and incorrect mode is specified, will throw an error'):
            sample_list = [1,2,3,1,4]
            sla = slay.Slay(sample_list)
            expect(sla.ch_dup(sample_list,"L")).to(equal("Invalid Mode"))